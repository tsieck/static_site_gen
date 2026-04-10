import unittest
from extract_markdown_images import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )
    
    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "Here is ![one](https://a.com/1.png) and ![two](https://a.com/2.png)"
        )
        self.assertListEqual(
            [
                ("one", "https://a.com/1.png"),
                ("two", "https://a.com/2.png"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")],
            matches,
        )
    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "Links: [one](https://a.com) and [two](https://b.com)"
        )
        self.assertListEqual(
            [
                ("one", "https://a.com"),
                ("two", "https://b.com"),
            ],
            matches,
        )
    def test_extract_markdown_links_ignores_images(self):
        matches = extract_markdown_links(
            "An image ![img](https://a.com/x.png) and a link [site](https://b.com)"
        )
        self.assertListEqual(
            [("site", "https://b.com")],
            matches,
        )