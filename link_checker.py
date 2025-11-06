#!/usr/bin/env python3
"""
Markdown Link Checker
A simple tool to check for broken links in Markdown files.
Usage: python link_checker.py <markdown_file>
"""

import sys
import requests
import re
from urllib.parse import urlparse

def extract_links(markdown_text):
    """Extract all links from markdown text."""
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(link_pattern, markdown_text)

def check_link(url):
    """Check if a URL is reachable."""
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400
    except requests.RequestException:
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python link_checker.py <markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)

    links = extract_links(content)
    broken_links = []

    for text, url in links:
        if not url.startswith('http'):
            continue  # Skip relative or anchor links
        if not check_link(url):
            broken_links.append((text, url))

    if broken_links:
        print("Broken links found:")
        for text, url in broken_links:
            print(f"- [{text}]({url})")
    else:
        print("All links are working!")

if __name__ == "__main__":
    main()