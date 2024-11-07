class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # HTML tag element e.g. "p", "a", etc.
        self.value = value
        self.children = children # HTML children elements
        self.props = props # dictionary with attributes e.g. "href": "google.com"


    def to_html(self):
        # meant to be overridden by child classes
        raise NotImplementedError
    

    def props_to_html(self):
        return_string = ""
        for value in self.props:
            return_string += f' {value}="{self.props[value]}"'
        return return_string
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
        raise ValueError("Tried to equate HTMLNode and non-HTMLNode objects")

    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"