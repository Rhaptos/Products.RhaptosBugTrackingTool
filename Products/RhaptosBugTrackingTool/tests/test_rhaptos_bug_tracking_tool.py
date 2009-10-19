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


from Products.PloneTestCase import PloneTestCase

import patch_zope_testing


_PRODUCTS = ('Products.RhaptosBugTrackingTool',)
_PROFILES = ('Products.RhaptosBugTrackingTool',)
PloneTestCase.setupPloneSite(products=_PRODUCTS, extension_profiles=_PROFILES)


class TestRhaptosBugTrackingTool(PloneTestCase.PloneTestCase):

    def test_fail(self):
        pass
