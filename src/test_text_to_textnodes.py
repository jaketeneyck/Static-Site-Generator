import unittest

from text_to_textnodes import *


class TestSplitNodesFuncs(unittest.TestCase):
    def test_text_to_textnodes(self):
        input = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(expected, text_to_textnodes(input))


    def test_text_to_textnodes_bold_code(self):
        # testing for a smaller use case, just bold and code blocks
        result = text_to_textnodes("This is **bold** and `code`")
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    def test_text_to_textnode_only_text(self):
        result = text_to_textnodes("This is only regular text")
        expected = [
            TextNode("This is only regular text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_to_textnode_link_first(self):
        # Testing for when normal text is not the first thing is the input
        result = text_to_textnodes("[This link](https://boot.dev) is to boot.dev, **wow**")
        expected = [
            TextNode("This link", TextType.LINK, "https://boot.dev"),
            TextNode(" is to boot.dev, ", TextType.NORMAL),
            TextNode("wow", TextType.BOLD)
        ]
        self.assertEqual(result, expected)

    def test_text_to_textnode_just_image(self):
        # Testing for just an image node
        result = text_to_textnodes("![This is obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        expected = [
            TextNode("This is obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(result, expected)

        
if __name__ == "__main__":
    unittest.main()