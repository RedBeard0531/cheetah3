#!/usr/bin/env python
# -*- coding: utf8 -*-

from Cheetah.Template import Template
import traceback
import unittest_local_copy as unittest # This is stupid

class JPQ_UTF8_Test1(unittest.TestCase):
    def runTest(self):
        t = Template.compile(source="""Main file with |$v|

        $other""")

        otherT = Template.compile(source="Other template with |$v|")
        other = otherT()
        t.other = other

        t.v = u'Unicode String'
        t.other.v = u'Unicode String'

        assert t()

class JPQ_UTF8_Test2(unittest.TestCase):
    def runTest(self):
        t = Template.compile(source="""Main file with |$v|

        $other""")

        otherT = Template.compile(source="Other template with |$v|")
        other = otherT()
        t.other = other

        t.v = u'Unicode String with eacute é'
        t.other.v = u'Unicode String'

        assert unicode(t())
        assert t().__str__()


class JPQ_UTF8_Test3(unittest.TestCase):
    def runTest(self):
        t = Template.compile(source="""Main file with |$v|

        $other""")

        otherT = Template.compile(source="Other template with |$v|")
        other = otherT()
        t.other = other

        t.v = u'Unicode String with eacute é'
        t.other.v = u'Unicode String and an eacute é'

        assert unicode(t())

class JPQ_UTF8_Test4(unittest.TestCase):
    def runTest(self):
        t = Template.compile(source="""Main file with |$v| and eacute in the template é""")

        t.v = 'Unicode String'

        assert t()

class JPQ_UTF8_Test5(unittest.TestCase):
    def runTest(self):
        t = Template.compile(source="""#encoding utf-8
        Main file with |$v| and eacute in the template é""")

        t.v = u'Unicode String'

        print t()

if __name__ == '__main__':
    unittest.main()