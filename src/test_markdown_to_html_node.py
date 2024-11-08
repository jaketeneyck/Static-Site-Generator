import unittest

from markdown_to_html_node import *


class TestSplitNodesFuncs(unittest.TestCase):
    def test_markdown_to_html_node_1(self):
        input = '''# Heading with **bold**

> This is a quote.
> Still part of the quote.

- Item 1 with *italic*
- Item 2

This is a paragraph of text. It has multiple sentences.'''

        node = markdown_to_html_node(input)
        # Test the root node
        self.assertEqual(node.tag, "div")
        
        # Test the children count
        self.assertEqual(len(node.children), 4)  # heading, quote, list, paragraph
        
        # Test specific nodes
        self.assertEqual(node.children[0].tag, "h1")
        self.assertEqual(node.children[1].tag, "blockquote")
        self.assertEqual(node.children[2].tag, "ul")

#     def test_markdown_to_html_node_2(self):
#         input = '''### This is a heading 3 with **bold and *italic* writing**

#         > This is a quote
#         > continued with *italic and **bold** tags*

# ###### This is a heading 6 tag

# # This is a heading 1 tag
# '''
#         node = markdown_to_html_node(input)

#         # Test children count
#         self.assertEqual(len(node.children), 4)

#         # Test specific nodes
#         self.assertEqual(node.children[0].tag, "h3")
#         self.assertEqual(node.children[1].tag, "blockquote")
#         self.assertEqual(node.children[2].tag, "h6")
#         self.assertEqual(node.children[3].tag, "h1")

    def test_markdown_to_html_3(self):
        input = '''**Hello *world***'''
        print(markdown_to_html_node(input)) 
        print("\n")
        print(markdown_to_html_node(input).to_html())


if __name__ == "__main__":
    unittest.main()