from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children == None:
            raise ValueError("ParentNode must have children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        elif len(self.children) == 0:
            raise ValueError("ParentNode must have more than 0 children")
        else:
            htmlstring = f'<{self.tag}>'
            childhtmlstrings = []
            for child in self.children:
                # Base case for recursive call
                if type(child) == LeafNode:
                    childhtmlstrings.append(child.to_html())
                elif type(child) == ParentNode:
                    results = []
                    if child.children != None and child.tag != None:
                        for grandchild in child.children:
                            results.append(grandchild.to_html())
                    childhtmlstrings.append(f'<{child.tag}>{"".join(results)}</{child.tag}>')
            htmlstring += "".join(childhtmlstrings) + f"</{self.tag}>"
            return htmlstring

