from textnode import *
from parentnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        # Do not strip the text to preserve whitespace
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i, section_text in enumerate(sections):
            if i % 2 == 0:
                split_nodes.append(TextNode(section_text, TextType.NORMAL))
            else:
                split_nodes.append(TextNode(section_text, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes