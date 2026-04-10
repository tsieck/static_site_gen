from parentnode import ParentNode
from textnode import TextNode, TextType
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        paragraph = " ".join(block.split("\n"))
        return ParentNode("p", text_to_children(paragraph))

    if block_type == BlockType.HEADING:
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break
        text = block[level + 1:]
        return ParentNode(f"h{level}", text_to_children(text))

    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(line.lstrip(">").strip())
        quote_text = " ".join(new_lines)
        return ParentNode("blockquote", text_to_children(quote_text))

    if block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            children.append(ParentNode("li", text_to_children(line[2:])))
        return ParentNode("ul", children)

    if block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            children.append(ParentNode("li", text_to_children(line[3:])))
        return ParentNode("ol", children)

    if block_type == BlockType.CODE:
        text = block[4:-3]
        text_node = TextNode(text, TextType.TEXT)
        code_node = text_node_to_html_node(text_node)
        return ParentNode("pre", [ParentNode("code", [code_node])])

    raise ValueError("invalid block type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode("div", children)