#!/usr/bin/env python3
"""
Simple URL Shortener
Stores URLs in a local file.
Usage: python url_shortener.py [shorten <url> | get <short>]
"""

import sys
import json
import os
import hashlib

URL_FILE = 'urls.json'

def load_urls():
    """Load URLs."""
    if os.path.exists(URL_FILE):
        with open(URL_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_urls(urls):
    """Save URLs."""
    with open(URL_FILE, 'w') as f:
        json.dump(urls, f)

def shorten_url(url):
    """Shorten URL."""
    short = hashlib.md5(url.encode()).hexdigest()[:6]
    urls = load_urls()
    urls[short] = url
    save_urls(urls)
    print(f"Short URL: {short}")

def get_url(short):
    """Get full URL."""
    urls = load_urls()
    if short in urls:
        print(urls[short])
    else:
        print("URL not found.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python url_shortener.py [shorten <url> | get <short>]")
        sys.exit(1)
    command = sys.argv[1]
    if command == 'shorten':
        shorten_url(sys.argv[2])
    elif command == 'get':
        get_url(sys.argv[2])
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()