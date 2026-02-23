import unittest
from block import markdown_to_blocks, block_to_block_type, BlockType

class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_type_heading(self):
        heading = "# Heading"
        type = block_to_block_type(heading)
        self.assertEqual(type, BlockType.HEADING)

    def test_block_type_code(self):
        code = "```\n code block \n```"
        type = block_to_block_type(code)
        self.assertEqual(type, BlockType.CODE)

    def test_block_type_quote(self):
        quote = "> Quote\n> lines\n> here"
        type = block_to_block_type(quote)
        self.assertEqual(type, BlockType.QUOTE)

    def test_block_type_unordered_list(self):
        list = "- Item\n- Another Item\n- A third item"
        type = block_to_block_type(list)
        self.assertEqual(type, BlockType.UNORDERED_LIST)

    def test_block_type_ordered_list(self):
        list = "1. One\n2. Two\n3. Three"
        type = block_to_block_type(list)
        self.assertEqual(type, BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()