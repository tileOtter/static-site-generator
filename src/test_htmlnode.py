import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("img", "alt text", {"src": "cat.png", "alt": "A cat"})
        html = node.to_html()
        # Don’t assert exact order if you’re not sure – maybe just:
        self.assertIn('src="cat.png"', html)
        self.assertIn('alt="A cat"', html)
        self.assertTrue(html.startswith("<img"))
        self.assertTrue(html.endswith("</img>"))

    def test_leaf_to_html_raises_without_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
         node.to_html()