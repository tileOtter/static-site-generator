from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_nodes = node.text.split(delimiter)
            if len(split_nodes)%2 == 0:
                raise Exception("Invalid Markdown: missing closing delimiter")
            for i in range(len(split_nodes)):
                if split_nodes[i] == "":
                    continue
                if i%2 != 0:
                    new_nodes.append(TextNode(split_nodes[i], text_type))
                else:
                    new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
    return new_nodes