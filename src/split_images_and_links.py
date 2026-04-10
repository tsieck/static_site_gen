from extract_markdown_images import extract_markdown_images,extract_markdown_links
from textnode import TextNode,TextType



def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        for image_alt, image_link in images:
            image_markdown = f"![{image_alt}]({image_link})"
            sections = text.split(image_markdown, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not found")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            text = sections[1]

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"
            sections = text.split(link_markdown, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, link not found")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            text = sections[1]

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes