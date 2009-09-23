
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.interfaces import IBody
from Products.GenericSetup.interfaces import INode
from Products.GenericSetup.utils import XMLAdapterBase
from Products.GenericSetup.utils import PropertyManagerHelpers
from Products.RhaptosBugTrackingTool.interfaces.portal_bugtracking import portal_bugtracking as IBugTrackingTool
from zope.app import zapi

filename = 'rhaptos_bugtracker.xml'

def importBugTrackingTool(context):
    portal = context.getSite()
    logger = context.getLogger('bugtracker')
    tool = getToolByName(portal, 'portal_bugtracking')

    body = context.readDataFile(filename)
    if body is None:
        logger.info('Nothing to import.')
        return
    
    importer = zapi.queryMultiAdapter((tool, context), IBody)
    if importer is None:
        logger.warning('Import adapter missing.')
        return

    importer.body = body
    logger.info('Bug tracking tool imported.')


def exportBugTrackingTool(context):
    portal = context.getSite()
    logger = context.getLogger('bugtracker')
    tool = getToolByName(portal, 'portal_bugtracking', None)
    if tool is None:
        logger.info('Nothing to export.')
        return

    exporter = zapi.queryMultiAdapter((tool, context), IBody)
    if exporter is None:
        logger.warning('Export adapter missing.')
        return

    context.writeDataFile(filename, exporter.body, exporter.mime_type)
    logger.info('Bug tracking tool exported.')


class BugTrackingToolXMLAdapter(XMLAdapterBase, PropertyManagerHelpers):

    __used_for__ = IBugTrackingTool

    def _exportNode(self):
        """Export the object as a DOM node.
        """
        #self._doc = doc
        node = self._getObjectNode('object')
        node.appendChild(self._extractProperties())
        return node

    def _importNode(self, node):
        """Import the object from the DOM node.
        """
        self._initProperties(node)

    node = property(_exportNode, _importNode)

