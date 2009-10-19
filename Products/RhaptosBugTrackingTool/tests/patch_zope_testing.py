#------------------------------------------------------------------------------#
#   patch_zope_testing.py                                                      #
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
"""Monkey patch for zope.testing to get it to properly format exceptions.
$Id: $
"""


import zope.exceptions

def format_exception(t, v, tb, limit=None):
    fmt = zope.exceptions.exceptionformatter.TextExceptionFormatter(
        limit=None)
    return fmt.formatException(t, v, tb)

from zope.testing.testrunner import tb_format
tb_format.format_exception = format_exception
