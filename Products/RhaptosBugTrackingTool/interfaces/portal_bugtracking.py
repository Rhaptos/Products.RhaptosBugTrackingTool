# Copyright (c) 2004 The Connexions Project, All Rights Reserved
# Written by Lorne Wilson

""" Bug Tracking interface"""

from Interface import Attribute
try:
    from Interface import Interface
except ImportError:
    # for Zope versions before 2.6.0
    from Interface import BugTracking as Interface

class portal_bugtracking(Interface):
    """Defines an interface for a tool that submits bugs to a bugtracking system"""

    id = Attribute('id','Must be set to "portal_bugtracking"')
    def submitBug(self, summary, email, name=None, contentUrl=None, bugType='Unknown', severity='minor', description=None):
        """
        Submit a bug into the bug tracking system
        """

