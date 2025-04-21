import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src")))
from htmlnode import LeafNode
from textnode import TextTypes,TextNode

TEXT_TYPE_TO_HTML = {
    "text": (None,{}),
    "bold": ("b",{}),
    "italic": ("i",{}),
    "code": ("code",{}),
    "link": ("a",{"href": lambda text_node: text_node.url}),
    "image": ("img",{"src": lambda text_node:text_node.url,"alt": lambda text_node:text_node.text})
}


def text_node_to_html_node(text_node):
       if text_node.text_type.value not in TEXT_TYPE_TO_HTML:
           raise Exception("wrong type")
       tag, props = TEXT_TYPE_TO_HTML[text_node.text_type.value]
       prop = {key: func(text_node) if callable(func) else func for key,func in props.items()}
       if tag == "img":
           return LeafNode(tag,"",prop)
       return LeafNode(tag,text_node.text,prop)
   
def split_nodes_delimiter(old_node,delimiter,text_type):
    
    
    final_list = []
    for node in old_node:
        if node.text_type != TextTypes.TEXT:
            final_list.append(node)
            continue
        
        num = node.text.count(delimiter)
        if num %2 != 0:
            raise Exception("delimiter doesn't match")
        num = 0
        splitted_text = node.text.split(delimiter)
        for i in range(len(splitted_text)):
            
            if splitted_text[i] == '':
                continue
            if i % 2 != 0:
                final_list.append(TextNode(splitted_text[i], text_type))     
            else:
                final_list.append(TextNode(splitted_text[i], TextTypes.TEXT))
                
        
    return final_list
        
        
       
            
            