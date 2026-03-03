import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

xml_file = "WordPress.2026-03-03.xml"
output_file = "exported_posts.txt"

tree = ET.parse(xml_file)
root = tree.getroot()

namespaces = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/'
}

with open(output_file, "w", encoding="utf-8") as f:
    for item in root.findall(".//item"):
        post_type = item.find("wp:post_type", namespaces)
        status = item.find("wp:status", namespaces)

        if post_type is not None and post_type.text == "post" and status.text == "publish":
            title = item.find("title").text or ""
            content = item.find("content:encoded", namespaces).text or ""

            clean_text = BeautifulSoup(content, "html.parser").get_text()

            f.write(title + "\n")
            f.write("=" * len(title) + "\n\n")
            f.write(clean_text + "\n\n\n")

print("Done. File saved as:", output_file)