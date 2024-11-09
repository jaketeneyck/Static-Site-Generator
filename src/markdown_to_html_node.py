from block_functions import block_to_block_type, markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from text_to_html import *
from parentnode import *
from leafnode import *
from textnode import *
import re

block_type_paragraph = "PARAGRAPH"
block_type_heading = "HEADING"
block_type_code = "CODE"
block_type_quote = "QUOTE"
block_type_olist = "ORDERED_LIST"
block_type_ulist = "UNORDERED_LIST"

def markdown_to_html_node(markdown):
    nodes = [] # main list of nodes to be returned at the end

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        type = block_to_block_type(block)
        nodes.append(block_to_node(block, type))

    return ParentNode("div", nodes) # wrap the html in a div tag and return


def block_to_node(block, block_type):
    match block_type:
        case "HEADING":
            return heading_node(block)
        case "CODE":
            return code_node(block)
        case "QUOTE":
            return quote_node(block)
        case "UNORDERED_LIST":
            return unordered_list_node(block)
        case "ORDERED_LIST":
            return ordered_list_node(block)
        case "PARAGRAPH":
            return ParentNode("p", text_to_children(block))
        case _:
            raise Exception("Invalid block type")


def text_to_children(text):
    # use the text to textnodes function, then loop through each node and convert to htmlnode
    children = []
    textnodes = text_to_textnodes(text)
    for node in textnodes:
        children.append(text_node_to_html_node(node))

    return children  


def collect_html_tags(nodes):
    value = ""
    for node in nodes:
        if isinstance(node, LeafNode):
            value += node.to_html()
        else:
            value += node

    return value


def heading_node(block):
    count = block.count("#") # get number of hashtags for what level header it is
    temp = block.replace("#", "", count).strip()
    children = text_to_children(temp)
    return HTMLNode(f"h{count}", None, children)


def code_node(block):
    children = text_to_children(block)
    value = collect_html_tags(children)
    return HTMLNode("pre", None, [HTMLNode("code", value, children)])


def quote_node(block):
    lines = block.splitlines()
    new_lines = []

    # clean the lines of all > characters before splitting the text for child tags
    for line in lines:
        new_lines.append(line.lstrip(">").lstrip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return HTMLNode("blockquote", None, children)

def unordered_list_node(block):
    nodes = []
    lines = block.splitlines()
    for line in lines:
        content = line.lstrip(' -').strip()
        content = content.lstrip(' *').strip()
        if content:
            children = text_to_children(content)
            nodes.append(HTMLNode("li", None, children))
        
    return ParentNode("ul", nodes)


def ordered_list_node(block):
    nodes = []
    lines = block.splitlines()
    for line in lines:
        content = re.sub(r'^\s*\d+\.\s?', '', line)
        content.lstrip()
        if content:
            children = text_to_children(content)
            nodes.append(HTMLNode("li", None, children))
        
    return ParentNode("ol", nodes)