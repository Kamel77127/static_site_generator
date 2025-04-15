import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    
    def test_props(self):
        node = HtmlNode("<a>" , "http://kamel.fr", None ,{"href" : "http://kamel.fr", "target": "_blank"})
        print(node)
        



        