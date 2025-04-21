import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src/utility")))
from textnode import TextNode,TextTypes
from utility import text_node_to_html_node,split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node1 = TextNode("_this_ is a bold text node", TextTypes.TEXT)
        node2 = TextNode("this _is_ a link ndoe", TextTypes.TEXT)
        node4 = TextNode("this _is an image_", TextTypes.TEXT)
        print(split_nodes_delimiter([node1,node2,node4],"_",TextTypes.ITALIC))
        
        
if __name__ == "__main__":
    unittest.main()
    