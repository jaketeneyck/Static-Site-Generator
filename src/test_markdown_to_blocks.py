import unittest
import markdown

from markdown_to_blocks import *


class TestLeafNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        result = markdown_to_blocks('''# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item''')
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]


        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()