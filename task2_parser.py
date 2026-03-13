from bs4 import BeautifulSoup

# a) Read the HTML text as a string
html_doc = """
<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their
names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# b) Parse using BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print("--- BeautifulSoup Approach ---")

# i. All href links in the given html text
print("\nAll href links:")
a_tags = soup.find_all('a')
for tag in a_tags:
    print(tag.get('href'))

# ii. All class values for <a> tags
print("\nAll class values for <a> tags:")
for tag in a_tags:
    # BeautifulSoup returns classes as a list because HTML elements can have multiple classes
    print(tag.get('class'))

#Custom recursive approach without using BeautifulSoup
import re

def recursive_html_parser(html_string, hrefs=None, classes=None):
    """
    Recursively scans an HTML string for <a> tags to extract href and class attributes.
    """
    # Initialize lists on the first call
    if hrefs is None:
        hrefs = []
    if classes is None:
        classes = []

    # Find the starting index of the next <a> tag
    start_tag_idx = html_string.find("<a ")
    
    # Base case: If no more <a> tags are found, return the collected lists
    if start_tag_idx == -1:
        return hrefs, classes

    # Find the end of this specific opening tag (">")
    end_tag_idx = html_string.find(">", start_tag_idx)
    
    # Failsafe for malformed HTML missing a closing bracket
    if end_tag_idx == -1:
        return hrefs, classes

    # Isolate the text inside the opening tag (e.g., '<a href="..." class="...">')
    tag_content = html_string[start_tag_idx:end_tag_idx]

    # Use basic regex to pull out the attribute values from this isolated string
    href_match = re.search(r'href=["\']([^"\']+)["\']', tag_content)
    if href_match:
        hrefs.append(href_match.group(1))

    class_match = re.search(r'class=["\']([^"\']+)["\']', tag_content)
    if class_match:
        # Splitting the string into a list to mimic how BeautifulSoup handles classes
        classes.append(class_match.group(1).split())

    # Recursive step: Call the function again, passing the remainder of the HTML string
    remaining_html = html_string[end_tag_idx:]
    return recursive_html_parser(remaining_html, hrefs, classes)

# Execute the recursive function
print("\n--- Custom Recursive Approach ---")
extracted_hrefs, extracted_classes = recursive_html_parser(html_doc)

print("\nAll href links:")
for href in extracted_hrefs:
    print(href)

print("\nAll class values for <a> tags:")
for cls in extracted_classes:
    print(cls)