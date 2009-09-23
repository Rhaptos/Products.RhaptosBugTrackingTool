"""
Rhaptos BugTracking Product

Author: Kyle Clarkson and Lorne Wilson
(C) 2005 Rice University

This software is subject to the provisions of the GNU Lesser General
Public License Version 2.1 (LGPL).  See LICENSE.txt for details.
"""

import AccessControl
import xmlrpclib
from Products.CMFCore.utils import UniqueObject
from OFS.SimpleItem import SimpleItem
from Globals import InitializeClass
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.CMFCore.CMFCorePermissions import ManagePortal
from interfaces.portal_bugtracking import portal_bugtracking as IBugTrackingTool
from OFS.PropertyManager import PropertyManager


class BugTrackingTool(UniqueObject, SimpleItem, PropertyManager):

    __implements__ = (IBugTrackingTool)

    id = 'portal_bugtracking'
    meta_type = 'BugTracking Tool'
    security = AccessControl.ClassSecurityInfo()
    
    # ZMI methods
    manage_options=(( {'label':'Overview',   'action':'manage_overview'},
                      {'label':'Properties', 'action':'manage_propertiesForm'},
                    )
                    + SimpleItem.manage_options
                    )

    #def __init__(self):	
    #    self.trac_dir = '/opt/trac/tracdev'
    ##   ZMI methods
    security.declareProtected(ManagePortal, 'manage_overview')
    manage_overview = PageTemplateFile('zpt/explainBugTrackingTool', globals() )

    # IBugTrackingTool Interface fulfillment 
        
    def submitBug(self, summary, email, name=None, contentUrl=None, bugType='Unknown', severity='minor', description=None):
        """
        Submit a bug to the trac system
        """
        if not hasattr(self, 'trac_xmlrpc'):
            raise ValueError, "Trac_xmlrpc is not configured"
        trac_xmlrpc = getattr(self,'trac_xmlrpc')
        
        # Set some default values for properties that can be over_written
        if hasattr(self, 'trac_type'):
            trac_type = getattr(self, 'trac_type')
        else:
            trac_type = 'defect'
            
        if hasattr(self, 'trac_state'):
            trac_state = getattr(self, 'trac_state')
        else:
            trac_state = 'new'
            
        server = xmlrpclib.ServerProxy(trac_xmlrpc)
        attributes = {};
        attributes['version'] = 'Live'
        attributes['type'] = trac_type
        attributes['status'] = trac_state
        attributes['summary'] = summary
        attributes['keywords'] = 'ReportABug'
        if name and email:
            attributes['reporter'] = '%s <%s>' % (name, email)
        elif name:
            attributes['reporter'] = name
        elif email:
            attributes['reporter'] = email
        if description:
            attributes['description'] = description
        attributes['severity'] = severity
        if contentUrl:
            attributes['contentobj'] = contentUrl
        attributes['area'] = bugType

        # Create ticket through XML-RPC. The "True" is for the "notify" parameter.
        newid = server.ticket.create(summary, description, attributes, True)
        return (newid)


InitializeClass(BugTrackingTool)


# Convenience functions

   
