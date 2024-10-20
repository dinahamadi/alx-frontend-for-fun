#!/usr/bin/python3
"""
This script takes 2 arguments:
First argument is the name of the Markdown file.
Second argument is the output file name.
"""

import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]
    try:
        with open(markdown_file, 'r') as f:
            pass
    except FileNotFoundError:
        sys.stderr.write("Missing {}\n".format(markdown_file))
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
