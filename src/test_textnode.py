import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq_text(self):
        node = TextNode("hello", TextType.TEXT)
        node2 = TextNode("goodbye", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_type(self):
        node1 = TextNode("hello", TextType.TEXT)
        node2 = TextNode("hello", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_url(self):
        node1 = TextNode("hello", TextType.LINK, "google.com")
        node2 = TextNode("hello", TextType.LINK, "boot.dev")
        self.assertNotEqual(node1, node2)
   
    def test_eq_with_none_url(self):
        node1 = TextNode("hello", TextType.TEXT)
        node2 = TextNode("hello", TextType.TEXT, None)
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()