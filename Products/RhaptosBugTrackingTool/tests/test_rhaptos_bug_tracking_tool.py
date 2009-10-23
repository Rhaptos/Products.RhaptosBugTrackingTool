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


import Products.RhaptosBugTrackingTool

from Products.RhaptosTest import base


base.PRODUCTS_TO_LOAD_ZCML = [('configure.zcml', Products.RhaptosBugTrackingTool),]
base.PRODUCTS_TO_INSTALL = ['Products.RhaptosBugTrackingTool',]


class TestRhaptosBugTrackingTool(base.RhaptosTestCase):

    def test_pass(self):
        assert 1 == 1

    def test_interface(self):
        """Make sure the interfaces are correctly being implemented."""
        from zope.interface.verify import verifyClass
        from zope.interface import Interface
        from Products.RhaptosBugTrackingTool.BugTrackingTool import BugTrackingTool
        self.assertTrue(verifyClass(Interface, BugTrackingTool))

    def test_bug_tracking_tool(self):
        from Products.RhaptosBugTrackingTool.BugTrackingTool import BugTrackingTool
        portal_bugtracking = BugTrackingTool()
        self.assertEqual(portal_bugtracking.id, 'portal_bugtracking')
        self.assertEqual(portal_bugtracking.meta_type, 'BugTracking Tool')


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestRhaptosBugTrackingTool))
    return suite
