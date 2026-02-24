from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    stripped_blocks = []
    for block in blocks:
        b = block.strip()
        if b:
            stripped_blocks.append(b)
    return stripped_blocks

def block_to_block_type(md_block):
    lines = md_block.split("\n")
    prefix = lines[0].split(" ")[0]
    if all(c == "#" for c in prefix) and len(prefix) >= 1 and len(prefix) <= 6 and lines[0].startswith(prefix + " "):
        return BlockType.HEADING
    if lines[0] == "```" and lines[-1] == "```" and len(lines) > 2:
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
