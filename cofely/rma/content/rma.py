"""Definition of the RMA content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cofely.rma import rmaMessageFactory as _

from cofely.rma.interfaces import IRMA
from cofely.rma.config import PROJECTNAME

from DateTime.DateTime import DateTime
from Products.CMFCore.utils  import getToolByName
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import DisplayList

from cofely.rma.permissions import viewRma
from cofely.rma.permissions import editRma

from cofely.rma.permissions import viewRepairingReport
from cofely.rma.permissions import editRepairingReport

from cofely.rma.permissions import viewArrivalDate
from cofely.rma.permissions import editArrivalDate

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column

RMASchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'rmaNumber',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"RMA number"),
            description=_(u"Unique number for the RMA item, should be auto \
                            generated."),
            visible={'edit': 'invisible', 'view': 'visible'},
        ),
        required=True,
        searchable=True,
        default_method="generateUniqueNumber",
    ),


    atapi.StringField(
        'company',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Company"),
            description=_(u"Name of the company that is sending an item \
                            back."),
            visible={'edit': 'invisible', 'view': 'visible'},
        ),
        required=True,
        searchable=True,
        default_method="getAccountCompany",
    ),


    atapi.StringField(
        'companyContact',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Company contact"),
            description=_(u"The person to contact for this item."),
        ),
        required=True,
        searchable=True,
        default_method="getAccountName",
    ),


    atapi.StringField(
        'companyPhone',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Phonenumber"),
            description=_(u"Phone number of the contact."),
        ),
        required=True,
        default_method="getAccountPhone",
    ),


    atapi.StringField(
        'deliveryStreet',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Street"),
            description=_(u"Street of your delivery adress."),
        ),
        required=True,
        default_method="getAccountDeliveryStreet",
    ),


    atapi.StringField(
        'deliveryPostalcode',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Postalcode"),
            description=_(u"Postalcode of your delivery adress."),
        ),
        required=True,
        default_method="getAccountDeliveryPostalcode",
    ),


    atapi.StringField(
        'deliveryCity',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"City"),
            description=_(u"City of your delivery adress."),
        ),
        required=True,
        default_method="getAccountDeliveryCity",
    ),


    atapi.StringField(
        'deliveryCountry',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Country"),
            description=_(u"Country of your delivery adress."),
        ),
        required=True,
        default_method="getAccountDeliveryCountry",
    ),


    atapi.StringField(
        'customerReference',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Referencenumber customer"),
            description=_(u"Customer's own reference number."),
        ),
        required=True,
        searchable=True,
    ),


    atapi.StringField(
        'title',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Item"),
            description=_(u"Name or type of item that is being returned."),
        ),
        required=True,
        searchable=True,
        accessor="Title",
    ),


    atapi.StringField(
        'productType',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.SelectionWidget(
            label=_(u"Product type"),
            description=_(u"What kind of item is this?"),
            format="select",
        ),
        required=True,
        vocabulary="getProductTypeList"
    ),


    atapi.StringField(
        'typeNumber',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Type number"),
            description=_(u"Type number of item that is being returned."),
        ),
        required=False,
        searchable=True,
    ),

    atapi.StringField(
        'serialNumber',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.StringWidget(
            label=_(u"Serial number"),
            description=_(u"Serial number of item that is being returned. This field is required if 'Speed control' is chosen as 'Product type'."),
        ),
        required=False,
        searchable=True,
    ),


    atapi.TextField(
        'description',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.TextAreaWidget(
            label=_(u"Complaint"),
            description=_(u"What's wrong with the item you are returning?"),
        ),
        required=True,
        searchable=True,
        accessor="Description",
    ),


    atapi.BooleanField(
        'warranty',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRma,
        write_permission=editRma,
        widget=atapi.BooleanWidget(
            label=_(u"Warranty"),
            description=_(u"Do you want to claim a warranty?"),
        ),
        required=False,
    ),


    atapi.DateTimeField(
        'arrivalDate',
        storage=atapi.AnnotationStorage(),
        view_permission=viewArrivalDate,
        write_permission=editArrivalDate,
        widget=atapi.CalendarWidget(
            label=_(u"Arrival date"),
            description=_(u"Date that the RMA arrived back."),
            show_hm=False,
            format='%d-%m-%Y',
        ),
        validators=('isValidDate'),
    ),

    atapi.TextField(
        'arrivalDescription',
        storage=atapi.AnnotationStorage(),
        view_permission=viewArrivalDate,
        write_permission=editArrivalDate,
        widget=atapi.TextAreaWidget(
            label=_(u"Arrival Description"),
            description=_(u"In which repair rack was the item put."),
        ),
        required=False,
        searchable=True,
    ),

    atapi.TextField(
        'repairingReport',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRepairingReport,
        write_permission=editRepairingReport,
        widget=atapi.TextAreaWidget(
            label=_(u"Repair report"),
            description=_(u"Text that outlines the action that was taken \
                            to 'fix' the RMA."),
        ),
        required=False,
        searchable=True,
    ),

    DataGridField('usedMaterials',
        view_permission=viewRepairingReport,
        write_permission=editRepairingReport,
        columns=("amount", "material"),
        allow_empty_rows = False,
        widget = DataGridWidget(
        label=_(u"Used materials"),
            description=_(u"Materials used fo repair the item."),
            columns={
                'amount': Column(_(u"Amount")),
                'material': Column(_(u"Material")),
                },
        ),
        required=False,
        searchable=True,
    ),

    atapi.IntegerField(
        'repairingHours',
        storage=atapi.AnnotationStorage(),
        view_permission=viewRepairingReport,
        write_permission=editRepairingReport,
        widget=atapi.IntegerWidget(
            label=_(u"Hours worked"),
            description=_(u"Hours worked to 'fix' the RMA."),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

RMASchema['title'].storage = atapi.AnnotationStorage()
RMASchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(RMASchema, moveDiscussion=False)


class RMA(base.ATCTContent):
    """Create a new RMA"""
    implements(IRMA)

    meta_type = "RMA"
    schema = RMASchema
    security = ClassSecurityInfo()

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    repairingReport = atapi.ATFieldProperty('repairingReport')

    repairingHours = atapi.ATFieldProperty('repairingHours')

    customerReference = atapi.ATFieldProperty('customerReference')

    rmaNumber = atapi.ATFieldProperty('rmaNumber')

#    complaint = atapi.ATFieldProperty('complaint')

    productType = atapi.ATFieldProperty('productType')

    typeNumber = atapi.ATFieldProperty('typeNumber')

    serialNumber = atapi.ATFieldProperty('serialNumber')

    warranty = atapi.ATFieldProperty('warranty')

    company = atapi.ATFieldProperty('company')

    companyContact = atapi.ATFieldProperty('companyContact')

    companyPhone = atapi.ATFieldProperty('companyPhone')

    deliveryStreet = atapi.ATFieldProperty('deliveryStreet')

    deliveryPostalcode = atapi.ATFieldProperty('deliveryPostalcode')

    deliveryCity = atapi.ATFieldProperty('deliveryCity')

    deliveryCountry = atapi.ATFieldProperty('deliveryCountry')

    arrivalDate = atapi.ATFieldProperty('arrivalDate')

    arrivalDescription = atapi.ATFieldProperty('arrivalDescription')

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('generateUniqueNumber')

    def generateUniqueNumber(self):
        """
        Generate a unique number.
        Just get the current date/time and convert it into an integer, so it
        should always be unique.
        """
        return int(DateTime())

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getAccountName')

    def getAccountName(self):
        """
        Get the fullname of the member.
        """
        mt = getToolByName(self, 'portal_membership')
        if mt.isAnonymousUser():  # the user has not logged in
            return None
        else:
            member = mt.getAuthenticatedMember()
            username = member.getUserName()
            fullname = mt.getMemberInfo(username).get('fullname', '')
            return fullname

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getAccountCompany')

    def getAccountCompany(self):
        """
        Get of the member.
        """
        mt = getToolByName(self, 'portal_membership')
        if mt.isAnonymousUser():  # the user has not logged in
            return None
        else:
            member = mt.getAuthenticatedMember()
            street = member.getProperty('companyName')
            return street

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getAccountPhone')

    def getAccountPhone(self):
        """
        Get of the member.
        """
        mt = getToolByName(self, 'portal_membership')
        if mt.isAnonymousUser():  # the user has not logged in
            return None
        else:
            member = mt.getAuthenticatedMember()
            street = member.getProperty('companyPhone')
            return street

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getAccountDeliveryStreet')

    def getAccountDeliveryStreet(self):
        """
        Get of the member.
        """
        mt = getToolByName(self, 'portal_membership')
        if mt.isAnonymousUser():  # the user has not logged in
            return None
        else:
            member = mt.getAuthenticatedMember()
            street = member.getProperty('deliveryStreet')
            return street

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getAccountDeliveryPostalcode')

    def getAccountDeliveryPostalcode(self):
        """
        Get of the member.
        """
        mt = getToolByName(self, 'portal_membership')
        if mt.isAnonymousUser():  # the user has not logged in
            return None
        else:
            member = mt.getAuthenticatedMember()
            postalcode = member.getProperty('deliveryPostalcode')
            return postalcode

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getAccountDeliveryCity')

    def getAccountDeliveryCity(self):
        """
        Get of the member.
        """
        mt = getToolByName(self, 'portal_membership')
        if mt.isAnonymousUser():  # the user has not logged in
            return None
        else:
            member = mt.getAuthenticatedMember()
            city = member.getProperty('deliveryCity')
            return city

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getAccountDeliveryCountry')

    def getAccountDeliveryCountry(self):
        """
        Get of the member.
        """
        mt = getToolByName(self, 'portal_membership')
        if mt.isAnonymousUser():  # the user has not logged in
            return None
        else:
            member = mt.getAuthenticatedMember()
            country = member.getProperty('deliveryCountry')
            return country

    # Declare function to be inaccessible to restricted code.
    security.declarePrivate('getProductTypeList')

    def getProductTypeList(self):
        """
        Return al list of product types.
        """
        return DisplayList((
                ('gtv', 'GTV'),
                ('vergrendelmagneten', 'Vergrendelmagneten'),
                ('toerenregelingen', 'Toerenregelingen'),
                ('motoren', 'Motoren'),
                ('overige', 'Overige'),
               ))


atapi.registerType(RMA, PROJECTNAME)
