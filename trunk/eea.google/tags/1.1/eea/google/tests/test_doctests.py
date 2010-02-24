""" Doc tests
"""
import unittest
from zope.testing import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite as Suite
from base import GoogleFunctionalTestCase

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

def test_suite():
    """ Suite
    """
    return unittest.TestSuite((
            Suite('README.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.google',
                  test_class=GoogleFunctionalTestCase) ,
            Suite('docs/api.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.google',
                  test_class=GoogleFunctionalTestCase) ,
            Suite('docs/analytics.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.google',
                  test_class=GoogleFunctionalTestCase) ,
            Suite('docs/tool.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.google',
                  test_class=GoogleFunctionalTestCase) ,
    ))
