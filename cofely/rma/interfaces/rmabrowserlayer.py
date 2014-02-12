from zope.interface import Interface
# -*- Additional Imports Here -*-


class IRMABrowserLayer(Interface):
    """
    A layer specific for this add-on product.

    This interface is referred in browserlayers.xml.

    All views and viewlets register against this layer will appear on your Plone site
    only when the add-on installer has been run.
    """

    # -*- schema definition goes here -*-
