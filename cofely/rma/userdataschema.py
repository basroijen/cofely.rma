from zope.interface import Interface, implements
from zope import schema
from plone.app.users.userdataschema import IUserDataSchemaProvider, IUserDataSchema

# -*- Message Factory Imported Here -*-
from cofely.rma import rmaMessageFactory as _


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """
    Use all the fields from the default user data schema, and add various
    extra fields.
    """
    companyName = schema.TextLine(
        title=_(u'label_companyName', default=u'Company Name'),
        description=_(u'help_companyName',
                      default=u"Name of your company"),
        required=True,
        )

    companyPhone = schema.TextLine(
        title=_(u'label_companyPhonenumber', default=u'Company Phonenumber'),
        description=_(u'help_companyPhone',
                      default=u"Phonenumber of your company"),
        required=True,
        )

    companyFax = schema.TextLine(
        title=_(u'label_companyFax', default=u'Company Faxnumber'),
        description=_(u'help_companyFax',
                      default=u"Faxnumber of your company"),
        required=True,
        )

    deliveryStreet = schema.TextLine(
        title=_(u'label_deliveryStreet', default=u'Delivery Street'),
        description=_(u'help_deliveryStreet',
                      default=u"Street of your default delivery adress"),
        required=True,
        )

    deliveryPostalcode = schema.TextLine(
        title=_(u'label_deliveryPostalcode', default=u'Delivery Postal code'),
        description=_(u'help_deliveryPostalcode',
                      default=u"Postalcode of your default delivery adress."),
        required=True,
        )

    deliveryCity = schema.TextLine(
        title=_(u'label_deliveryCity', default=u'Delivery City'),
        description=_(u'help_deliveryCity',
                      default=u"City of your default delivery adress."),
        required=True,
        )

    deliveryCountry = schema.TextLine(
        title=_(u'label_deliveryCountry', default=u'Delivery Country'),
        description=_(u'help_deliveryCountry',
                      default=u"Country of your default delivery adress."),
        required=True,
        )
