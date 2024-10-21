import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq_blank(self):
        node = LeafNode()
        node2 = LeafNode()
        self.assertEqual(node, node2)

    def test_eq_full(self):
        children = [HTMLNode()]
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        node1 = HTMLNode("p", "This is a HTML node", children, props)
        node2 = HTMLNode("p", "This is a HTML node", children, props)
        self.assertEqual(node1, node2)

    def test_to_html(self):
        expected = "HTMLNode(None, None, None, None)"
        node = HTMLNode()
        self.assertEqual(expected, node.__repr__())
    
    def test_props_to_html(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        node = HTMLNode(None, None, None, props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, node.props_to_html())

if __name__ == "__main__":
    unittest.main()