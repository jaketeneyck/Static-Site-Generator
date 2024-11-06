from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):   
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            params = {}
            params["href"]= text_node.url
            return LeafNode(tag="a", value=text_node.text, props=params)
        case TextType.IMAGE:
            params = {}
            params["src"] = text_node.url
            params["alt"] = text_node.text
            return LeafNode(tag="img", value="", props=params)
        case _:
            raise Exception("Invalid text type for text node")
