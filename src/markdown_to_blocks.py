def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")

    cleaned_blocks = []

    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            lines = stripped.split("\n")
            normalized = "\n".join(line.strip() for line in lines)
            cleaned_blocks.append(normalized)

    return cleaned_blocks