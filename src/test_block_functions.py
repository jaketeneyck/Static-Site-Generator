import unittest

from block_functions import *


class TestBlockFunctions(unittest.TestCase):
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

    def test_block_to_block_type_heading_1(self):
        result = block_to_block_type('''# This is a heading''')
        expected = "HEADING"
        self.assertEqual(result, expected)

    def test_block_to_block_type_heading_6(self):
        result = block_to_block_type('''###### This is a heading''')
        expected = "HEADING"
        self.assertEqual(result, expected)

    def test_block_to_block_type_heading_7(self):
        result = block_to_block_type('''####### This is a heading''')
        expected = "PARAGRAPH"
        self.assertEqual(result, expected)

    def test_block_to_block_type_code(self):
        result = block_to_block_type('''```This is a code block```''')
        expected = "CODE"
        self.assertEqual(result, expected)

    def test_block_to_block_type_quotes_single(self):
        result = block_to_block_type('''>This a single line quote''')
        expected = "QUOTE"
        self.assertEqual(result, expected)

    def test_block_to_block_type_quotes_multi(self):
        result = block_to_block_type('''>This a multi line quote
                                     >Hopefully this works''')
        expected = "QUOTE"
        self.assertEqual(result, expected)

    def test_block_to_block_type_quotes_error(self):
        result = block_to_block_type('''>This a multi line quote
                                     

                                     >Hopefully this works''')
        expected = "PARAGRAPH"
        self.assertEqual(result, expected)

    def test_block_to_block_type_unordered_1(self):
        result = block_to_block_type('''- This is an unordered list
                                     - with
                                      - multiple lines''')
        expected = "UNORDERED_LIST"
        self.assertEqual(result, expected)

    def test_block_to_block_type_unordered_2(self):
        result = block_to_block_type('''* This is an unordered list
                                     * with
                                      * multiple lines''')
        expected = "UNORDERED_LIST"
        self.assertEqual(result, expected)

    def test_block_to_block_type_unordered_3(self):
        result = block_to_block_type('''- This is an unordered list
                                     * with
                                      - multiple lines''')
        expected = "UNORDERED_LIST"
        self.assertEqual(result, expected)

    def test_block_to_block_type_unordered_4(self):
        result = block_to_block_type('''- This is an unordered list
                                     * with an empty line

                                      - that should make it a paragraph''')
        expected = "PARAGRAPH"
        self.assertEqual(result, expected)

    def test_block_to_block_type_ordered_1(self):
        result = block_to_block_type('''1. This is an ordered list
                                     2. With multiple
                                     3. Lines''')
        expected = "ORDERED_LIST"
        self.assertEqual(result, expected)

    def test_block_to_block_type_ordered_2(self):
        result = block_to_block_type('''1. This is an ordered list
                                     21. With multiple
                                     3. Lines''')
        expected = "PARAGRAPH"
        self.assertEqual(result, expected)

    def test_block_to_block_type_paragraph(self):
        result = block_to_block_type('''This is a paragraph''')
        expected = "PARAGRAPH"
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()