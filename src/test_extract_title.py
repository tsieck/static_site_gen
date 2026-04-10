import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_raises(self):
        md = "## Not an h1"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_with_whitespace(self):
        md = "#   Tolkien Fan Club   "
        self.assertEqual(extract_title(md), "Tolkien Fan Club")