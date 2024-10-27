from textnode import *
from extract_markdown import *

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        image_props = extract_markdown_images(node.text)
        sections = []

        if len(image_props) == 0: # case for 0 images found
            new_nodes.append(node)

        elif len(image_props) == 1: # case for 1 image found
            sections = node.text.split(f"![{image_props[0][0]}]({image_props[0][1]})", 1)
            results = [
                TextNode(sections[0], "normal"),
                TextNode(image_props[0][0], TextType.IMAGE, image_props[0][1]),
                TextNode(sections[1], "normal")
            ]
            # Ensure no nodes with no text are added
            for r in results:
                if r.text != None:
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

            # Ensure no nodes with no text are added
            print(results)
            for r in results:
                if r.text != None:
                    new_nodes.append(r)
    return new_nodes

def split_nodes_link(old_nodes):
    pass