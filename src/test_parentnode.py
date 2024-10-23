import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],)
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(expected, node.to_html())

if __name__ == "__main__":
    unittest.main()