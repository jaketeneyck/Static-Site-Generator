from textnode import *
from parentnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if isinstance(node, TextNode):
            if node.text_type != TextType.NORMAL:
                if delimiter in node.text:
                    split_node = node.text.split(delimiter)
                    if len(split_node) % 2 == 0:
                        raise Exception("Invalid markdown syntax: no closing delimiter")
                    for i in range(0, len(split_node)):
                        if i % 2 == 0:
                            new_nodes.append(TextNode(split_node[i], node.text_type))
                        else:
                            child_node = TextNode(split_node[i], text_type)
                            parent_node = ParentNode(node.text_type, [child_node])
                            new_nodes.append(parent_node)
                else:
                    new_nodes.append(node)
            else:
                split_node = node.text.split(delimiter)
                if len(split_node) % 2 == 0:
                    raise Exception("Invalid markdown syntax: no closing delimiter")
                for i in range(0, len(split_node)):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(split_node[i], TextType.NORMAL))
                    else:
                        new_nodes.append(TextNode(split_node[i], text_type))
        elif isinstance(node, ParentNode):
            temp = ParentNode(node.tag, split_nodes_delimiter(node.children, delimiter, text_type)) 
            new_nodes.append(temp)

    return new_nodes