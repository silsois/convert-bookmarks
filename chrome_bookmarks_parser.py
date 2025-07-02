# chrome_bookmarks_parser.py
import json
import sys

def parse_bookmarks(bookmark_node, indent=0):
    html = ""
    if bookmark_node["type"] == "folder":
        html += " " * indent + '<DT><H3>{}</H3>\n'.format(bookmark_node["name"])
        html += " " * indent + "<DL><p>\n"
        for child in bookmark_node.get("children", []):
            html += parse_bookmarks(child, indent + 4)
        html += " " * indent + "</DL><p>\n"
    elif bookmark_node["type"] == "url":
        html += ' ' * indent + '<DT><A HREF="{}">{}</A>\n'.format(
            bookmark_node["url"], bookmark_node["name"]
        )
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python chrome_bookmarks_parser.py Bookmarks [output.html]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "bookmarks_converted.html"
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    html = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
"""
    roots = data["roots"]
    for root in ["bookmark_bar", "other", "synced"]:
        if root in roots:
            html += parse_bookmarks(roots[root], 4)
    html += "</DL><p>\n"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Bookmarks exported to {output_file}")

if __name__ == "__main__":
    main()
