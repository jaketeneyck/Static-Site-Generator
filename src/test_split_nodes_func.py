import unittest

from textnode import TextNode, TextType
from split_nodes_funcs import *


class TestSplitNodesFuncs(unittest.TestCase):

    # ----
    # Testing split images function
    # ----

    def test_split_nodes_images_none(self):
        node = TextNode(
            "This is a text node with no images", TextType.NORMAL
        )
        expected = [
            TextNode("This is a text node with no images", TextType.NORMAL)
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_split_nodes_images_one(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.NORMAL
        )
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif")
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_split_nodes_images_two(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL,
        )
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_split_nodes_images_first(self):
        # Tests for when the image link is first in the list of nodes
        node = TextNode(
            "![This](https://i.imgur.com/aKaOqIh.gif) is a rick roll", TextType.NORMAL
        )
        expected = [
            TextNode("This", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" is a rick roll", TextType.NORMAL)
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_split_nodes_images_second(self):
        # Tests for when there are two image links which come before the string nodes
        node = TextNode(
            "![This](https://i.imgur.com/aKaOqIh.gif) is a rick roll and ![this](https://i.imgur.com/fJRm4Vk.jpeg) is obi wan", TextType.NORMAL
        )
        expected = [
            TextNode("This", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" is a rick roll and ", TextType.NORMAL),
            TextNode("this", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" is obi wan", TextType.NORMAL)
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_split_nodes_images_multi(self):
        # Tests for when multiple nodes are passed into the function
        nodes = [
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL,),
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL,)
        ]
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(expected, split_nodes_image(nodes))

    # ----
    # Testing split links function
    # ----

    def test_split_nodes_links_none(self):
        node = TextNode("This is a text node with no links", TextType.NORMAL)
        expected = [
            TextNode("This is a text node with no links", TextType.NORMAL)
        ]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_split_nodes_links_one(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.NORMAL,
        )
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_split_nodes_links_two(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_split_nodes_links_first(self):
        # Tests for when the image link is first in the list of nodes
        node = TextNode(
            "[This](https://i.imgur.com/aKaOqIh.gif) is a rick roll", TextType.NORMAL
        )
        expected = [
            TextNode("This", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" is a rick roll", TextType.NORMAL)
        ]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_split_nodes_links_second(self):
        # Tests for when there are two image links which come before the string nodes
        node = TextNode(
            "[This](https://i.imgur.com/aKaOqIh.gif) is a rick roll and [this](https://i.imgur.com/fJRm4Vk.jpeg) is obi wan", TextType.NORMAL
        )
        expected = [
            TextNode("This", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" is a rick roll and ", TextType.NORMAL),
            TextNode("this", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" is obi wan", TextType.NORMAL)
        ]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_split_nodes_links_multi(self):
        # Tests for when multiple nodes are passed into the function
        nodes = [
            TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL,),
            TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL,)
        ]
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(expected, split_nodes_link(nodes))


if __name__ == "__main__":
    unittest.main()