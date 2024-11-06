from block_functions import block_to_block_type, markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from text_to_html import *
from parentnode import *
from leafnode import *
from textnode import *

def markdown_to_html_node(markdown):
    nodes = [] # main list of nodes to be returned at the end

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        type = block_to_block_type(block)
        nodes.append(block_to_node(block, type))

    return ParentNode("div", nodes) # wrap the html in a div tag and return


def block_to_node(block, block_type):
    # create the children list using text_to_children()
    children = text_to_children(block)

    match block_type:
        case "HEADING":
            return heading_node(block)
        case "CODE":
            return ParentNode("pre", ParentNode("code", children))
        case "QUOTE":
            return ParentNode("blockquote", children)
        case "UNORDERED_LIST":
            return unordered_list_node(children)
        case "ORDERED_LIST":
            return ordered_list_node(children)
        case "PARAGRAPH":
            return ParentNode("p", children)
        case _:
            raise Exception("Invalid block type")


def text_to_children(text):
    # use the text to textnodes function, then loop through each node and convert to htmlnode
    children = []
    textnodes = text_to_textnodes(text)
    for node in textnodes:
        children.append(text_node_to_html_node(node))

    return children  


def heading_node(block):
    children = text_to_children(block)
    count = block.count("#") # get number of hashtags for what level header it is
    value = children[0].value.replace("#", "")
    temp = block.replace("#", "", count).strip()
    children = text_to_children(temp)
    for i in range(1, len(children)):
        if isinstance(children[i], LeafNode):
            value += children[i].to_html()
        else:
            value += children[i]
    return HTMLNode(f"h{count}", value, children)


def unordered_list_node(children):
    nodes = []
    for child in children:
        nodes.append(ParentNode("li", child))
    return ParentNode("ul", nodes)


def ordered_list_node(children):
    nodes = []
    for child in children:
        nodes.append(ParentNode("li", child))
    return ParentNode("ol", nodes)
    

def main(): # for testing
    # input = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    input = "## This is an h2 *heading* tag"
    print(block_to_node(input, "HEADING"))

main()