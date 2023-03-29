#!/usr/bin/env python3

import argparse
import requests
import re

parser = argparse.ArgumentParser(description="Find JavaScript files containing a specific keyword from a list of URLs")
parser.add_argument("-f", "--file", help="File containing URLs to check", required=True)
parser.add_argument("-k", "--keyword", help="Keyword to search for in JavaScript files", required=True)
parser.add_argument("-t", "--timeout", help="Request timeout in seconds (default: 5)", type=int, default=5)
args = parser.parse_args()

def get_javascript_urls(url):
    try:
        response = requests.get(url, timeout=args.timeout)
    except:
        print("Failed to get page " + url)
        return []

    urls = re.findall('src="(.*?\.js)"', response.text)

    # Convert relative URLs to absolute URLs
    base_url = "/".join(url.split("/")[:-1])
    urls = [base_url + "/" + u if u.startswith("/") else u for u in urls]

    return urls

def search_for_keyword(url, keyword):
    try:
        response = requests.get(url, timeout=args.timeout)
    except:
        return False

    return keyword in response.text

with open(args.file, "r") as f:
    urls = [line.strip() for line in f]

javascript_urls = []

for url in urls:
    for js_url in get_javascript_urls(url):
        if search_for_keyword(js_url, args.keyword):
            print("Found keyword \"" + args.keyword + "\" in " + js_url)
            javascript_urls.append(js_url)

if len(javascript_urls) == 0:
    print("No JavaScript files containing \"" + args.keyword + "\" were found.")

