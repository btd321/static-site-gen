from textnode import TextNode
from textnode import TextType


def main():
    text_node = TextNode("This is some anchor text", TextType.LINK,"https://ww.boot.dev")
    print(text_node)

main()

