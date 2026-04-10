from textnode import TextNode,TextType
from split_images_and_links import split_nodes_links,split_nodes_image
from split_nodes_delimiter import split_nodes_delimiter



def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)

    return nodes