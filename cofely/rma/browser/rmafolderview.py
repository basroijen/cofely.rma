from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from cofely.rma import rmaMessageFactory as _

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage


class IRMAFolderView(Interface):
    """
    RMA Folder view interface
    """

    def recurse(self, show_history=False):
        """
        Returns first a status message and second the brains of
        portal type RMA.
        If select_wf is given, it is used as review_state, if not,
        all RMA's will be returned, respecting permissions of course!
        """


class RMAFolderView(BrowserView):
    """
    RMA Folder browser view
    """
    implements(IRMAFolderView)
    template = ViewPageTemplateFile('rmafolderview.pt')

    def __call__(self):
        if not self.request.has_key('form.button.submit'):
            status, self.log = self.recurse()
            # If create new button was used
            if self.request.has_key('form.button.create'):
                redirecturl = self.context.absolute_url() + \
                              '/createObject?type_name=RMA'
                self.request.response.redirect(redirecturl)
            # If no button was pushed, return
            return self.template()
        else:
            # Button was pushed, so show history
            status, self.log = self.recurse(show_history=True)
            IStatusMessage(self.request).addStatusMessage(status, type='info')
            return self.template()

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.log = []

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def recurse(self, show_history=False):
        """
        Returns first a status message and second the brains of portal type
        RMA.
        If select_wf is given, it is used as review_state, if not, all RMA's
        will be returned, respecting permissions of course!
        """
        if not show_history:
            brains = self.portal_catalog.searchResults(sort_on='getRmaNumber', sort_order='reverse', path={'query': \
                            (self.context.absolute_url_path())}, \
                            portal_type='RMA', review_state=('requested', 'arrived', 'in_repair_rack', 'in_repair', 'tender_approval', 'waiting_for_material', 'repaired', 'ready_for_dispatch'))
            status = _(u"Showing all open RMA's.")
        else:
            brains = self.portal_catalog.searchResults(sort_on='getRmaNumber', sort_order='reverse', path={'query': \
                            (self.context.absolute_url_path())}, \
                            portal_type='RMA', review_state='completed')
            status = _(u"Showing all completed RMA's.")
        return status, brains
