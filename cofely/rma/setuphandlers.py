import logging
from cofely.rma import config
from Products.CMFCore.utils import getToolByName

# The profile id of this package:
PROFILE_ID = 'profile-cofely.rma:default'


def add_catalog_indexes(context, logger=None):
    """
    Method to add our wanted indexes to the portal_catalog

    @parameters:

    When called from the import_various method below, 'context' is
    the plone site and 'logger' is the portal_setup logger. But
    this method can also be used as upgrade step, in which case
    'context' will be portal_setup and 'logger' will be None.
    """
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(config.PROJECTNAME)

    # Run the catalog.xml step as that may have defined new metadata
    # columns. We could instead add <depends name="catalog"/> to
    # the registration of our import step in zcml, but doing it in
    # code makes this method usable as upgrade step as well.
    # Remove these lines when you have no catalog.xml file
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = getToolByName(context, 'portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    # Note that changing a index_type of an existing index is NOT
    # provided here!
    wanted = (('getArrivalDate', 'DateIndex'),
              ('getCompany', 'FieldIndex'),
              ('getRmaNumber', 'FieldIndex'),
              ('getRepairingReport', 'FieldIndex'),
              ('getProductType', 'FieldIndex'),
              )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def import_various(context):
    """
    Import steps that are not handled in xml files.
    """
    # Only run step if a flag is present, because GS
    # will always try to run this, whatever product is imported
    if context.readDataFile('cofely.rma-default.txt') is None:
        return
    logger = context.getLogger(config.PROJECTNAME)
    site = context.getSite()
    add_catalog_indexes(site, logger)


def upgrade_various(context):
    """
    upgrade steps that are not handled in xml files.
    """
    add_catalog_indexes()
