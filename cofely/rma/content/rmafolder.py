"""Definition of the RMA folder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cofely.rma.interfaces import IRMAfolder
from cofely.rma.config import PROJECTNAME

RMAfolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

RMAfolderSchema['title'].storage = atapi.AnnotationStorage()
RMAfolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    RMAfolderSchema,
    folderish=True,
    moveDiscussion=False
)


class RMAfolder(folder.ATFolder):
    """Folder containing al the RMA's."""
    implements(IRMAfolder)

    meta_type = "RMAfolder"
    schema = RMAfolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(RMAfolder, PROJECTNAME)
