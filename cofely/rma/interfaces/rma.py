from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cofely.rma import rmaMessageFactory as _



class IRMA(Interface):
    """Create a new RMA"""

    # -*- schema definition goes here -*-
    repairingReport = schema.Text(
        title=_(u"Repair report"),
        required=False,
        description=_(u"Text that outlines the action that was taken to 'fix' the RMA."),
    )
#
    repairingHours = schema.Text(
        title=_(u"Hours worked"),
        required=False,
        description=_(u"Hours worked to 'fix' the RMA."),
    )
#
    rmaNumber = schema.TextLine(
        title=_(u"RMA number"),
        required=True,
        description=_(u"Unique number for the RMA item, should be auto generated."),
    )
#
    customerReference = schema.TextLine(
        title=_(u"Referencenumber customer"),
        required=True,
        description=_(u"Customer's own reference number."),
    )
#
    description = schema.Text(
        title=_(u"Complaint"),
        required=True,
        description=_(u"What's wrong with the item you are returning?"),
    )
#
    title = schema.TextLine(
        title=_(u"Item"),
        required=True,
        description=_(u"Name or type of item that is being returned."),
    )
#
    company = schema.TextLine(
        title=_(u"Company"),
        required=True,
        description=_(u"Name of the company that is sending an item back."),
    )
#
    companyContact = schema.TextLine(
        title=_(u"Company contact"),
        required=True,
        description=_(u"The person to contact for this item."),
    )
#
    companyPhone = schema.TextLine(
        title=_(u"Phonenumber"),
        required=True,
        description=_(u"Phone number of the contact."),
    )
#
    deliveryStreet = schema.TextLine(
        title=_(u"Street"),
        required=True,
        description=_(u"Street of your delivery adress."),
    )
#
    deliveryPostalcode = schema.TextLine(
        title=_(u"Postalcode"),
        required=True,
        description=_(u"Postalcode of your delivery adress."),
    )
#
    deliveryCity = schema.TextLine(
        title=_(u"City"),
        required=True,
        description=_(u"City of your delivery adress."),
    )
#
    deliveryCountry = schema.TextLine(
        title=_(u"Country"),
        required=True,
        description=_(u"Country of your delivery adress."),
    )
#
    arrivalDate = schema.Date(
        title=_(u"Arrival date"),
        required=False,
        description=_(u"Date that the RMA arrived back."),
    )
#
    arrivalDescription = schema.Text(
        title=_(u"Arrival Description"),
        required=False,
        description=_(u"In which repair rack was the item put."),
    )
#
    productType = schema.TextLine(
        title=_(u"Product type"),
        required=True,
        description=_(u"What kind of item is this?"),
    )
#
    typeNumber = schema.TextLine(
        title=_(u"Type number"),
        required=True,
        description=_(u"Type number of item that is being returned."),
    )
#
    serialNumber = schema.TextLine(
        title=_(u"Serial number"),
        required=False,
        description=_(u"Serial number of item that is being returned. This field is required if 'Speed control' is chosen as 'Product type'."),
    )
#
    warranty = schema.Bool(
        title=_(u"Warranty"),
        required=False,
        description=_(u"Do you want to claim a warranty?"),
    )
#
