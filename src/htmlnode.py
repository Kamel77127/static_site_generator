



class HtmlNode():
    
    
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
       html_text = ""
       if self.props == None:
           return html_text
       for item in self.props:
           html_text += f"{item}:'{self.props[item]}' "
       return html_text
            
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HtmlNode):
    
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value = value, props=props)   
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
        
    

class ParentNode(HtmlNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children = children, props = props)
    
    def to_html(self):
        result = f"<{self.tag}>"
        if not self.tag:
            raise ValueError("Tag needed")
        elif not self.children:
            raise ValueError("children needed")
        else:
            for item in self.children:
               result += item.to_html()
        return result + f"</{self.tag}>"
        