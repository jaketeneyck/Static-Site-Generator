import unittest

from markdown_to_html_node import *


class TestSplitNodesFuncs(unittest.TestCase):
    def test_markdown_to_html_node(self):
        input = '''# Heading

> This is a quote.
> Still part of the quote.

- Item 1
- Item 2

This is a paragraph of text. It has multiple sentences.'''

        print(markdown_to_html_node(input))
        
if __name__ == "__main__":
    unittest.main()