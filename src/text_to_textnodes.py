from textnode import *
from split_nodes_delimiter import *
from split_nodes_funcs import *

def text_to_textnodes(text):
    new_node = TextNode(text, TextType.NORMAL)
    italic_processed = []
    code_processed = []
    # Initial split on bold delimiter
    bold_processed = split_nodes_delimiter([new_node], "**", TextType.BOLD)

    # Process italics
    italic_processed.extend(split_nodes_delimiter(bold_processed, "*", TextType.ITALIC))

    # Process code blocks
    code_processed.extend(split_nodes_delimiter(italic_processed, "`", TextType.CODE))

    # Process links and images then return 
    nodes = split_nodes_link(split_nodes_image(code_processed))

    # Filter out any nodes with empty text before returning
    return [node for node in nodes if node.text != ""]