from Products.CMFCore.utils import getToolByName
#from Products.CMFPlone.utils import base_hasattr
from Products.CMFCore.WorkflowCore import WorkflowException
from Products.statusmessages.interfaces import IStatusMessage

from cofely.rma import rmaMessageFactory as _
from cofely.rma.tools import mailStatusUpdate

def updateWorkflowStatus(object, event):
    """
    Executed when a 'Employee' is edited or created.
    Check if the employee has the required subfolders
    Set the correct roles based on the 'user' field
    """
    pc = getToolByName(object, 'portal_catalog')
    workflowTool = getToolByName(object, "portal_workflow")

    status = workflowTool.getStatusOf("RMA_Proces_Workflow", object)
    # Plone workflows use variable called "review_state" to store state id
    # of the object state
    if not status:
        return

    state = status["review_state"]

    if state == "requested" and object.arrivalDate:
        try:
            if object.arrivalDescription:
                # We can also skip 'arrived' state
                workflowTool.doActionFor(object, "receivedProcessed")
            else:
                workflowTool.doActionFor(object, "received")
            #mailStatusUpdate(object.REQUEST)
            status = _(u"Customer has been informed of the status change.")
            IStatusMessage(object.REQUEST).addStatusMessage(status, type='info')
        except WorkflowException:
            # a workflow exception is risen if the state transition is not available
            # (the sampleProperty content is in a workflow state which
            # does not have a "submit" transition)
            pass

    if state == "arrived" and object.arrivalDescription:
        try:
            workflowTool.doActionFor(object, "processed")
            #mailStatusUpdate(object.REQUEST)
            status = _(u"Status has been updated.")
            IStatusMessage(object.REQUEST).addStatusMessage(status, type='info')
        except WorkflowException:
            # a workflow exception is risen if the state transition is not available
            # (the sampleProperty content is in a workflow state which
            # does not have a "submit" transition)
            pass

#    if state == "in_repair" and object.repairingReport.data:
#        try:
#            workflowTool.doActionFor(object, "completed")
#            #mailStatusUpdate(object.REQUEST)
#            status = _(u"Customer has been informed of the status change.")
#            IStatusMessage(object.REQUEST).addStatusMessage(status, type='info')
#        except WorkflowException:
#            # a workflow exception is risen if the state transition is not available
#            # (the sampleProperty content is in a workflow state which
#            # does not have a "submit" transition)
#            pass

def rmaAdded(object, event):
    """
    If an new RMA is added, send an e-mail to all users with role employee??
    """
    #mailStatusUpdate(object.REQUEST)
    status = _(u"The company has been informed of the status change.")
    IStatusMessage(object.REQUEST).addStatusMessage(status, type='info')
