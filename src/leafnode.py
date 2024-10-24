from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag=None, value=None, props=None):
        if value == None:
            raise ValueError("LeafNodes must have a value")
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value == None:
            raise ValueError("No value supplied, all leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"