#!/usr/bin/python3
"""
This script takes 2 arguments:
First argument is the name of the Markdown file.
Second argument is the output file name.
"""

import sys
import os


def parse_markdown_to_html(markdown_file, html_file):
    """Parse Markdown file and convert to HTML."""
    with open(markdown_file, 'r') as md_file, open(html_file, 'w') as html_f:
        in_list = False
        is_ordered_list = False
        for line in md_file:
            line = line.strip()
            if line.startswith('#'):
                if in_list:
                    html_f.write('</ol>\n' if is_ordered_list else '</ul>\n')
                    in_list = False
                heading_level = len(line.split()[0])
                if heading_level <= 6:
                    heading_content = line[heading_level:].strip()
                    html_f.write('<h{0}>{1}</h{0}>\n'.format(heading_level, heading_content))
            elif line.startswith('* ') or line.startswith('- '):
                if not in_list or (is_ordered_list and line.startswith('- ')):
                    if is_ordered_list:
                        html_f.write('</ol>\n')
                    html_f.write('<ul>\n')
                    in_list = True
                    is_ordered_list = False
                list_item_content = line[2:].strip()
                html_f.write('    <li>{}</li>\n'.format(list_item_content))
            elif line.startswith('1. '):  # Ordered list item
                if not in_list or (not is_ordered_list and line.startswith('- ')):
                    if not is_ordered_list:
                        html_f.write('</ul>\n')
                    html_f.write('<ol>\n')
                    in_list = True
                    is_ordered_list = True
                list_item_content = line[3:].strip()
                html_f.write('    <li>{}</li>\n'.format(list_item_content))
            else:
                if in_list:
                    html_f.write('</ol>\n' if is_ordered_list else '</ul>\n')
                    in_list = False
                if line:
                    # Add <br> for line breaks
                    html_f.write('<p>{}</p>\n'.format(line.replace('\n', '<br />')))

        if in_list:
            html_f.write('</ol>\n' if is_ordered_list else '</ul>\n')


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]
    parse_markdown_to_html(markdown_file, html_file)
    exit(0)
