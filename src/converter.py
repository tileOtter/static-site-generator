from block import markdown_to_blocks, block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType
import os

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    nodes = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            nodes.append(paragraph_block_to_htmlnode(block))
        elif block_to_block_type(block) == BlockType.HEADING:
            nodes.append(heading_block_to_htmlnode(block))
        elif block_to_block_type(block) == BlockType.CODE:
            nodes.append(code_block_to_htmlnode(block))
        elif block_to_block_type(block) == BlockType.QUOTE:
            nodes.append(quote_block_to_htmlnode(block))
        elif block_to_block_type(block) == BlockType.UNORDERED_LIST:
            nodes.append(unordered_list_block_to_htmlnode(block))
        elif block_to_block_type(block) == BlockType.ORDERED_LIST:
            nodes.append(ordered_list_block_to_htmlnode(block))
    return ParentNode("div", nodes)

def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        if textnode is not None:
            children.append(text_node_to_html_node(textnode))
    return children

def extract_title(md):
    title = md.splitlines()[0].rstrip()
    parts = title.split(" ", 1)
    if parts[0] != "#":
        raise Exception
    return parts[1]

def generate_page(from_path, template_path, dest_path):
    if not os.path.isfile(from_path):
        raise Exception("Source path invalid, not a file.")
    if not os.path.isfile(template_path):
        raise Exception("Template path invalid, not a file.")

    with open(from_path, 'r') as source:
        content = source.read()
    
    with open(template_path, 'r') as temp:
        template = temp.read()
    
    html_content = markdown_to_html_node(content)
    title = extract_title(content)
    page = template.replace('{{ Content }}', html_content.to_html()).replace('{{ Title }}', title)

    updated_path = os.path.splitext(dest_path)[0] + '.html'
    with open(updated_path, 'w') as destination:
        
        destination.write(page)

def generate_page_recursive(from_path, template_path, dest_path):
    for item in os.listdir(from_path):
        new_from = os.path.join(from_path, item)
        new_dest = os.path.join(dest_path, item)
        if os.path.isdir(new_from):
            os.makedirs(new_dest)
            generate_page_recursive(new_from, template_path, new_dest)
        else:
            generate_page(new_from, template_path, new_dest)

        # if directory, create dest dir and call generate_page_recursive with new paths
        # if file call generate_page with given paths
            
def paragraph_block_to_htmlnode(md_block):
    clean_block = md_block.replace("\n", " ")
    return ParentNode("p", text_to_children(clean_block))

def heading_block_to_htmlnode(md_block):
    length = md_block.split(" ", 1)
    return ParentNode(f"h{len(length[0])}", text_to_children(length[1]))

def code_block_to_htmlnode(md_block):
    stripped = md_block.removeprefix("```\n").removesuffix("```")
    textnode = TextNode(stripped, TextType.CODE)
    html = text_node_to_html_node(textnode)
    node = ParentNode("pre", [html])
    return node

def quote_block_to_htmlnode(md_block):
    lines = md_block.splitlines()
    clean_lines = []
    clean_block = ""
    for line in lines:
        clean_lines.append(line.replace("> ", "", 1))
    for line in clean_lines:
        clean_block += line + " "
    return ParentNode("blockquote", text_to_children(clean_block))

def unordered_list_block_to_htmlnode(md_block):
    lines = md_block.splitlines()
    clean_lines = []
    nodes = []
    for line in lines:
        clean_lines.append(line.replace("* ", "", 1).replace("- ", "", 1))
    for line in clean_lines:
        nodes.append(ParentNode("li", text_to_children(line)))
    return ParentNode("ul", nodes)

def ordered_list_block_to_htmlnode(md_block):
    lines = md_block.splitlines()
    nodes = []
    for line in lines:
        parts = line.split(". ", 1)
        if len(parts) > 1:
            content = parts[1]
            nodes.append(ParentNode("li", text_to_children(content)))
    return ParentNode("ol", nodes)