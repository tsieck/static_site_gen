

from textnode import TextNode, TextType
from markdown_to_html_node import markdown_to_html_node
import os
import shutil

def copy_dir_recursive(src, dst):
    items = os.listdir(src)

    for item in items:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            copy_dir_recursive(src_path, dst_path)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("no h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    content_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", content_html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)

    for item in items:
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(content_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(content_path, template_path, dest_path)

        elif item.endswith(".md"):
            dest_file_path = dest_path.replace(".md", ".html")
            generate_page(content_path, template_path, dest_file_path)



def main():
    if os.path.exists("public"):
        shutil.rmtree("public")

    os.mkdir("public")
    copy_dir_recursive("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()




