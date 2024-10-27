import re

def extract_markdown_images(text):
    html_tuples = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for m in matches:
        html_tuples.append((m[0], m[1]))
    
    return html_tuples


def extract_markdown_links(text):
    html_tuples = []
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for m in matches:
        html_tuples.append((m[0], m[1]))
    
    return html_tuples
