from textnode import *
from parentnode import *
from extract_markdown import *

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if isinstance(node, TextNode): # check if the node is a textnode
            image_props = extract_markdown_images(node.text)
            sections = []

            if len(image_props) == 0: # case for 0 images found
                new_nodes.append(node)

            elif len(image_props) == 1: # case for 1 image found
                sections = node.text.split(f"![{image_props[0][0]}]({image_props[0][1]})", 1)
                results = [
                    TextNode(sections[0], TextType.NORMAL),
                    TextNode(image_props[0][0], TextType.IMAGE, image_props[0][1]),
                    TextNode(sections[1], TextType.NORMAL)
                ]
                # Ensure no nodes with no text are added
                for r in results:
                    if r.text != None and r.text != "":
                        new_nodes.append(r)

            else: # case for more than 1 image found
                results = []
                # Process the string before the first image tag and the tag itself
                sections = node.text.split(f"![{image_props[0][0]}]({image_props[0][1]})", 1)
                results.append(TextNode(sections[0], TextType.NORMAL))
                results.append(TextNode(image_props[0][0], TextType.IMAGE, image_props[0][1]))

                for i in range(1, len(image_props)):
                    # Remove the first string and run splits on the second string
                    sections.pop(0)
                    sections = sections[0].split(f"![{image_props[i][0]}]({image_props[i][1]})", 1)
                    results.append(TextNode(sections[0], TextType.NORMAL))
                    results.append(TextNode(image_props[i][0], TextType.IMAGE, image_props[i][1]))
                
                # Add the last chunk of text if the image node comes first
                if len(sections) == 2:
                    results.append(TextNode(sections[1], TextType.NORMAL))

                # Ensure no nodes with no text are added
                for r in results:
                    if r.text != None and r.text != "":
                        new_nodes.append(r)

        elif isinstance(node, ParentNode): 
            # If it is a parent node, recursively call the function on its children
            processed_children = split_nodes_image(node.children)
            new_nodes.append(ParentNode(node.tag, processed_children))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if isinstance(node, TextNode):
            link_props = extract_markdown_links(node.text)
            sections = []

            if len(link_props) == 0: # case for 0 images found
                new_nodes.append(node)

            elif len(link_props) == 1: # case for 1 image found
                sections = node.text.split(f"[{link_props[0][0]}]({link_props[0][1]})", 1)
                results = [
                    TextNode(sections[0], TextType.NORMAL),
                    TextNode(link_props[0][0], TextType.LINK, link_props[0][1]),
                    TextNode(sections[1], TextType.NORMAL)
                ]
                # Ensure no nodes with no text are added
                for r in results:
                    if r.text != None and r.text != "":
                        new_nodes.append(r)

            else: # case for more than 1 image found
                results = []
                # Process the string before the first image tag and the tag itself
                sections = node.text.split(f"[{link_props[0][0]}]({link_props[0][1]})", 1)
                results.append(TextNode(sections[0], TextType.NORMAL))
                results.append(TextNode(link_props[0][0], TextType.LINK, link_props[0][1]))

                for i in range(1, len(link_props)):
                    # Remove the first string and run splits on the second string
                    sections.pop(0)
                    sections = sections[0].split(f"[{link_props[i][0]}]({link_props[i][1]})", 1)
                    results.append(TextNode(sections[0], TextType.NORMAL))
                    results.append(TextNode(link_props[i][0], TextType.LINK, link_props[i][1]))
                
                # Add the last chunk of text if the image node comes first
                if len(sections) == 2:
                    results.append(TextNode(sections[1], TextType.NORMAL))

                # Ensure no nodes with no text are added
                for r in results:
                    if r.text != None and r.text != "":
                        new_nodes.append(r)

        elif isinstance(node, ParentNode):
            # If it is a parent node, recursively call the function on its children
            processed_children = split_nodes_link(node.children)
            new_nodes.append(ParentNode(node.tag, processed_children))

    return new_nodes