from textnode import *

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # HTML tag element e.g. "p", "a", etc.
        self.value = value
        self.children = children # HTML children elements
        self.props = props # dictionary with attributes e.g. "href": "google.com"


    def to_html(self):
        # Case for just text
        if self.value != None and self.tag == None and self.children == None and self.props == None:
            return self.value
        else:
            if isinstance(self.tag, TextType):
                match self.tag:
                    case TextType.BOLD:
                        htmltag = "b"
                    case TextType.ITALIC:
                        htmltag = "i"
                    case TextType.IMAGE:
                        htmltag = "img"
                    case TextType.LINK:
                        htmltag = "a"
                    case TextType.CODE:
                        htmltag = "code"
            else:
                htmltag = self.tag
            # Add tag and props
            if self.props != None:
                htmlstring = f"<{htmltag}{self.props_to_html()}>"
            else:
                # Add just the tag
                htmlstring = f"<{htmltag}>"

            # Add value if it exists
            if self.value != None:
                htmlstring += self.value
        
            # Add child html to the string if necessary
            if self.children != None:
                if len(self.children) != 0:
                    for child in self.children:
                        htmlstring += child.to_html()
            
            # Add closing html tag and return
            htmlstring += f"</{htmltag}>"
            return htmlstring

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
    