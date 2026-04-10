import unittest
from blocktype import block_to_block_type, BlockType


class TestBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("## Heading"),
            BlockType.HEADING
        )

    def test_code(self):
        self.assertEqual(
            block_to_block_type("```\ncode\n```"),
            BlockType.CODE
        )

    def test_quote(self):
        self.assertEqual(
            block_to_block_type("> line1\n> line2"),
            BlockType.QUOTE
        )

    def test_unordered_list(self):
        self.assertEqual(
            block_to_block_type("- item1\n- item2"),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. one\n2. two"),
            BlockType.ORDERED_LIST
        )

    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("just text"),
            BlockType.PARAGRAPH
        )