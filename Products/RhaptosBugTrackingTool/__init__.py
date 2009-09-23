"""
Initialize RhaptosBugTracking Product

Author: Kyle Clarkson and Lorne Wilson
(C) 2005 Rice University

This software is subject to the provisions of the GNU Lesser General
Public License Version 2.1 (LGPL).  See LICENSE.txt for details.
"""

import sys
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
import BugTrackingTool

this_module = sys.modules[ __name__ ]
product_globals = globals()
tools = ( BugTrackingTool.BugTrackingTool,)

# Make the skins available as DirectoryViews
registerDirectory('skins', globals())

def initialize(context):
    utils.ToolInit('BugTracking Tool',
                    tools = tools,
                    product_name = 'RhaptosBugTrackingTool',
                    icon='tool.gif' 
                    ).initialize( context )
