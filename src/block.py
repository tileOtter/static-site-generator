def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    stripped_blocks = []
    for block in blocks:
        b = block.strip()
        if b:
            stripped_blocks.append(b)
    return stripped_blocks