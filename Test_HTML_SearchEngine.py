import unittest
from HTML_SearchEngine import *
import EnumTags

class Test_HTML_Search_Engine(unittest.TestCase):

    def test_choose_tag(self):
        ergebnis = "class_"
        s = HTML_SearchEngine()
        s.choose_Tag(1)

        self.assertEqual(ergebnis,s.show_Tag())

class Test_EnumTags(unittest.TestCase):

    def test_underscore(self):
        ergebnis = 1

        self.assertEqual(ergebnis, EnumTags.Tags.underscore_class.value)