import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_multiple_children(self):
        parent_node = ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " normal "),
            LeafNode("i", "italic"),
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold</b> normal <i>italic</i></p>",
        )