import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_basic(self):
        text = "This is plain text"
        nodes = text_to_textnodes(text)

        self.assertEqual(
            nodes,
            [TextNode("This is plain text", TextType.TEXT)]
        )

    def test_full_markdown(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![image](https://img.com/x.png) and a [link](https://boot.dev)"

        nodes = text_to_textnodes(text)

        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.com/x.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()