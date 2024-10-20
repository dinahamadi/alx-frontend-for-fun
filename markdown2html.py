#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

if not os.path.isfile(markdown_file):
    sys.stderr.write("Missing {}\n".format(markdown_file))
    sys.exit(1)

sys.exit(0)
