import unittest

from htmlnode import HTMLNODE


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNODE("p", "Hello")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")

    def test_non_eq(self):
        node = HTMLNODE(tag="p",value="This is an html node")
        node2 = HTMLNODE(tag="h1",value="This is an html node")
        self.assertNotEqual(node, node2)

    def test_with_props(self):
        node = HTMLNODE(tag="a",value="This is an html node",children=None,props={"href": "https://www.google.com","target":"_blank"})
        self.assertEqual(node.props,{"href": "https://www.google.com","target":"_blank"})


if __name__ == "__main__":
    unittest.main()