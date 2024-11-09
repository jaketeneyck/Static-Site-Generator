import unittest

from text_to_html import *


class TestTextToHTML(unittest.TestCase):
    def test_normal_text(self):
        node = TextNode("Testing text node", TextType.NORMAL)
        html = text_node_to_html_node(node) # convert text to html node
        expected = "Testing text node"
        self.assertEqual(expected, html.to_html())

    def test_bold(self):
        node = TextNode("Testing text node", TextType.BOLD)
        html = text_node_to_html_node(node)
        expected = "<strong>Testing text node</strong>"
        self.assertEqual(expected, html.to_html())

    def test_italic(self):
        node = TextNode("Testing text node", TextType.ITALIC)
        html = text_node_to_html_node(node)
        expected = "<em>Testing text node</em>"
        self.assertEqual(expected, html.to_html())

    def test_code(self):
        node = TextNode("Testing text node", TextType.CODE)
        html = text_node_to_html_node(node)
        expected = "<code>Testing text node</code>"
        self.assertEqual(expected, html.to_html())

    def test_link(self):
        node = TextNode("Testing text node", TextType.LINK, "https://www.google.com")
        html = text_node_to_html_node(node)
        expected = '<a href="https://www.google.com">Testing text node</a>'
        self.assertEqual(expected, html.to_html())

    def test_image(self):
        node = TextNode("Testing text node", TextType.IMAGE, "images/example.png")
        html = text_node_to_html_node(node)
        expected = '<img src="images/example.png" alt="Testing text node"></img>'
        self.assertEqual(expected, html.to_html())
    
    def test_invalid_type(self):
        node = TextNode("Testing text node", "bad value")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        

if __name__ == "__main__":
    unittest.main()