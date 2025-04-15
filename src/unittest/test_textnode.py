import unittest

from textnode import TextNode,TextTypes


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node1 = TextNode("this is a text ndoe", TextTypes.BOLD)
        node2 = TextNode("this is a text ndoe", TextTypes.BOLD)
        self.assertEqual(node1,node2)
        
        
if __name__ == "__main__":
    unittest.main()
    