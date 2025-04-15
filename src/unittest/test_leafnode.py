import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    
    
    def test_tohtml(self):
        node = LeafNode("p","bonjour je suis kamel",None,None)
        node2 = LeafNode("a","http:kamel.fr",None,{"href:":"hhtp.kamel.fr"})
        node3 = LeafNode("a",None,None,{"href:":"hhtp.kamel.fr"})
        print(node3.to_html())
        
        
        
if __name__ == "__main__":
    unittest.main()