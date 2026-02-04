import unittest

from htmlnode import HTMLNode

class TextHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value")
        node2 = HTMLNode("tag", "value")
        self.assertEqual(node, node2)

    def test_args(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_props(self):
        node = HTMLNode(None, None, None, {"testkey":"testvalue", "testkey1":"testvalue1"})
        print(node.props_to_html())
    
    def test_tohtml(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
