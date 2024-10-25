import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_normal(self):
        node = TextNode("This is a text node with no other tags", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.NORMAL)
        expected = [TextNode("This is a text node with no other tags", TextType.NORMAL)]
        self.assertEqual(new_nodes, expected)
    
    def test_bold(self):
        node = TextNode("This is a text node with **a bold** tag", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a text node with ", TextType.NORMAL),
            TextNode("a bold", TextType.BOLD),
            TextNode(" tag", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        node = TextNode("This is a text node with *an italic* tag", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is a text node with ", TextType.NORMAL),
            TextNode("an italic", TextType.ITALIC),
            TextNode(" tag", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, expected)
if __name__ == "__main__":
    unittest.main()