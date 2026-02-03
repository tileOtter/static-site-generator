from textnode import TextNode, TextType

def main():
    text = "I have a lovely bunch of coconuts."
    text_type = TextType.BOLD
    text_type2 = TextType.LINK
    url2 = "www.google.com"

    test = TextNode(text, text_type)
    test1 = TextNode(text, text_type2, url2)

    print(test)
    print(test1)

main()