from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.interfaces import IObjectPostValidation

# -*- Message Factory Imported Here -*-
from cofely.rma import rmaMessageFactory as _

from cofely.rma.interfaces import IRMA


class ValidateRequiredInput(object):
    """
    Checks if the SerialNumber field requires a value
    depending on the speedControl field
    """
    implements(IObjectPostValidation)
    adapts(IRMA)
    field_name = 'serialNumber'
    field_name_masterfield = 'productType'

    def __init__(self, context):
        self.context = context

    def __call__(self, request):
        value = request.form.get(self.field_name, request.get(self.field_name, None))
        requiredValue = request.form.get(self.field_name_masterfield, request.get(self.field_name_masterfield, None))
        if (value == '') and (requiredValue == 'gtv' or requiredValue == 'motoren' or requiredValue == 'toerenregelingen'):
            return {self.field_name: _(u"This field is required if 'speed control', 'GTV' or 'motoren' is chosen in the 'product type'-field.")}

        # Returning None means no error
        return None
