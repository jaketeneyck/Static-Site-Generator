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
        actual = text_to_textnodes(input)
        for i in range(0, len(expected)):
            print(f"Expected: {expected[i]} | Actual: {actual[i]}")
            print()

        self.assertEqual(input, text_to_textnodes(input))

if __name__ == "__main__":
    unittest.main()