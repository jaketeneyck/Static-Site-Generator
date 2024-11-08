from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import *

def text_node_to_html_node(text_node):   
    if isinstance(text_node, TextNode):
        match text_node.text_type:
            case TextType.NORMAL:
                return HTMLNode(None, text_node.text)
            case TextType.BOLD:
                return HTMLNode("strong", text_node.text)
            case TextType.ITALIC:
                return HTMLNode("em", text_node.text)
            case TextType.CODE:
                return HTMLNode("code", text_node.text)
            case TextType.LINK:
                params = {}
                params["href"]= text_node.url
                return HTMLNode(tag="a", value=text_node.text, props=params)
            case TextType.IMAGE:
                params = {}
                params["src"] = text_node.url
                params["alt"] = text_node.text
                return HTMLNode(tag="img", value="", props=params)
            case _:
                raise Exception("Invalid text type for text node")
    elif isinstance(text_node, ParentNode):
        children = []
        for child in text_node.children:
            children.append(text_node_to_html_node(child))
        return HTMLNode(text_node.tag, None, children)
        