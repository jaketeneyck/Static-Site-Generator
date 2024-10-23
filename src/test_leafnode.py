import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq_blank(self):
        node = LeafNode(value="value")
        node2 = LeafNode(value="value")
        self.assertEqual(node, node2)

    def test_to_html_no_tag(self):
        node = LeafNode(value="test")
        expected = "test"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_tag(self):
        node = LeafNode("p", "test")
        expected = "<p>test</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_tag_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()