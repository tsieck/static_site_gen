import unittest
from textnode import TextNode, TextType
from split_images_and_links import split_nodes_image, split_nodes_links


class Test_split_images_lins(unittest.TestCase):

    def test_split_images_single(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    def test_split_images_multiple(self):
        node = TextNode(
            "Start ![one](a.com/1.png) middle ![two](a.com/2.png) end",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("one", TextType.IMAGE, "a.com/1.png"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "a.com/2.png"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_images_none(self):
        node = TextNode("Just plain text", TextType.TEXT)

        new_nodes = split_nodes_image([node])

        self.assertListEqual([node], new_nodes)
    def test_split_images_non_text(self):
        node = TextNode("already image", TextType.IMAGE, "a.com/img.png")

        new_nodes = split_nodes_image([node])

        self.assertListEqual([node], new_nodes)
    def test_split_links_single(self):
        node = TextNode(
            "This is a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_links([node])

        self.assertListEqual(
            [
                TextNode("This is a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )
    def test_split_links_multiple(self):
        node = TextNode(
            "Go [one](a.com) and [two](b.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_links([node])

        self.assertListEqual(
            [
                TextNode("Go ", TextType.TEXT),
                TextNode("one", TextType.LINK, "a.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.LINK, "b.com"),
            ],
            new_nodes,
        )
    def test_split_links_none(self):
        node = TextNode("Just text", TextType.TEXT)

        new_nodes = split_nodes_links([node])

        self.assertListEqual([node], new_nodes)
    def test_split_links_non_text(self):
        node = TextNode("already link", TextType.LINK, "a.com")

        new_nodes = split_nodes_links([node])

        self.assertListEqual([node], new_nodes)
