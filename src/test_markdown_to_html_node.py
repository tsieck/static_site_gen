import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_heading(self):
        md = "# Hello"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(html, "<div><h1>Hello</h1></div>")

    def test_unordered_list(self):
        md = "- item1\n- item2"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>item1</li><li>item2</li></ul></div>"
        )

    def test_quote(self):
        md = "> line1\n> line2"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>line1 line2</blockquote></div>"
        )    