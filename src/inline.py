import re
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

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            current_text = node.text
            if not extract_markdown_images(current_text):
                new_nodes.append(node)
            else:
                for item in extract_markdown_images(current_text):
                    sections = current_text.split(f"![{item[0]}]({item[1]})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(item[0], TextType.IMAGE, item[1]))
                    current_text = sections[1]
                if current_text:
                    new_nodes.append(TextNode(current_text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            current_text = node.text
            if not extract_markdown_links(current_text):
                new_nodes.append(node)
            else:
                for item in extract_markdown_links(current_text):
                    sections = current_text.split(f"[{item[0]}]({item[1]})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(item[0], TextType.LINK, item[1]))
                    current_text = sections[1]
                if current_text:
                    new_nodes.append(TextNode(current_text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes