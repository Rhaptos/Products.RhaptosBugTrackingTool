#------------------------------------------------------------------------------#
#   test_rhaptos_bug_tracking_tool.py                                          #
#                                                                              #
#       Authors:                                                               #
#       Rajiv Bakulesh Shah <raj@enfoldsystems.com>                            #
#                                                                              #
#           Copyright (c) 2009, Enfold Systems, Inc.                           #
#           All rights reserved.                                               #
#                                                                              #
#               This software is licensed under the Terms and Conditions       #
#               contained within the "LICENSE.txt" file that accompanied       #
#               this software.  Any inquiries concerning the scope or          #
#               enforceability of the license should be addressed to:          #
#                                                                              #
#                   Enfold Systems, Inc.                                       #
#                   4617 Montrose Blvd., Suite C215                            #
#                   Houston, Texas 77006 USA                                   #
#                   p. +1 713.942.2377 | f. +1 832.201.8856                    #
#                   www.enfoldsystems.com                                      #
#                   info@enfoldsystems.com                                     #
#------------------------------------------------------------------------------#
"""Unit tests.
$Id: $
"""


from Products.RhaptosTest import config
import Products.RhaptosBugTrackingTool
config.products_to_load_zcml = [('configure.zcml', Products.RhaptosBugTrackingTool),]
config.products_to_install = ['RhaptosBugTrackingTool']
config.extension_profiles = ['Products.RhaptosBugTrackingTool:default']

from Products.CMFCore.utils import getToolByName
from Products.RhaptosBugTrackingTool.interfaces.portal_bugtracking import portal_bugtracking as IBugTrackingTool
from Products.RhaptosTest import base


class TestRhaptosBugTrackingTool(base.RhaptosTestCase):

    def afterSetUp(self):
        self.bug_tracker = getToolByName(self.getPortal(), 'portal_bugtracking')

    def beforeTearDown(self):
        pass

    def test_bug_tracker_interface(self):
        # Make sure that the bug tracker implements the expected interface.
        self.failUnless(IBugTrackingTool.isImplementedBy(self.bug_tracker))

    def test_bug_tracker_submit_bug(self):
        # FIXME:  I'm commenting out this test, because it actually creates
        # bugs in the Rhaptos Trac bug tracker.  Maybe it'd be useful to set up
        # a dummy Trac bug tracker only for testing purposes?  In any case,
        # currently, this tests passes...
        """
        summary = 'Hello, World!'
        email = 'raj@enfoldsystems.com'
        description = 'Hello, World!'
        id = self.bug_tracker.submitBug(summary, email, description=description)
        """

    def test_bug_tracker(self):
        self.assertEqual(1, 1)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestRhaptosBugTrackingTool))
    return suite
