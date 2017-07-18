#!/usr/bin/env python3

from css_html_js_minify import css_minify
import os

def minify_css():
    bundle_path = 'web/static/bundle/'

    if not os.path.exists(bundle_path):
        dir = os.path.dirname(bundle_path)
        os.makedirs(dir)
        print('Directory: {} created'.format(dir))

    with open('web/static/styles.css', 'r') as css_file:
        min_css = css_minify(css_file.read())

        with open('{}/styles.min.css'.format(bundle_path), 'w') as css_min_file:
            min = css_min_file.write(min_css)

if __name__ == '__main__':
    minify_css()
