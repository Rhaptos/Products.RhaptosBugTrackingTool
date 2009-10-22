#------------------------------------------------------------------------------#
#   base.py                                                                    #
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
"""Base class from which other Rhaptos unit test classes inherit.
$Id: $
"""


import patch_zope_testing

from Products.CMFPlone.tests import PloneTestCase
from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase.layer import PloneSite
from Testing import ZopeTestCase


PRODUCTS_TO_LOAD_ZCML = []
PRODUCTS_TO_INSTALL = []


class RhaptosTestCase(PloneTestCase.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            for zcml_file, product in PRODUCTS_TO_LOAD_ZCML:
                zcml.load_config(zcml_file, product)
            for product in PRODUCTS_TO_INSTALL:
                ZopeTestCase.installProduct(product)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass
