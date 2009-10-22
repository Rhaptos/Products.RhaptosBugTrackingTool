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

import patch_zope_testing

from Testing import ZopeTestCase

from Products.CMFPlone.tests import PloneTestCase
from Products.PloneTestCase.layer import PloneSite

from Products.Five import zcml
from Products.Five import fiveconfigure

import Products.RhaptosBugTrackingTool

class TestRhaptosBugTrackingTool(PloneTestCase.PloneTestCase):

    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml', Products.RhaptosBugTrackingTool)
            ZopeTestCase.installProduct('RhaptosBugTrackingTool')
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass

    def test_fake(self):
        pass

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestRhaptosBugTrackingTool))
    return suite

