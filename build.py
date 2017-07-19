#!/usr/bin/env python3
from css_html_js_minify import css_minify, html_minify
import os

cwd = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(cwd, '__source/templates/')
static_dir = os.path.join(cwd, '__source/static/')
bundle_dir = os.path.join(cwd, 'bundle/')


def compile_template(template, name):
    with open(templates_dir + '/layout.html', 'r') as f:
        layout = f.read()
        layout_start = layout.split("{% block container %}\n      {% endblock %}\n")

        with open(templates_dir + template, 'r') as h:
            home = h.read()

            home_start = home.split('{% block container %}')[1].split('{% endblock %}\n')[0]


        with open(name+'.html', 'w') as index:
            combile = index.write('{}{}{}'.format(layout_start[0], home_start, layout_start[1]))
            print('{} template is created'.format(name+'.html'))


def minify_css():
    if not os.path.exists(bundle_dir):
        dir = os.path.dirname(bundle_path)
        os.makedirs(dir)
        print('Directory: {} created'.format(dir))

    with open(static_dir + '/styles.css', 'r') as css_file:
        min_css = css_minify(css_file.read())

        with open(os.path.join(bundle_dir, 'styles.min.css'), 'w') as css_min_file:
            min = css_min_file.write(min_css)


def minify_html():
    html_files = os.listdir(cwd)

    for i in html_files:
        if i.endswith('.html'):
            with open(i, 'r') as html_file:
                min_html = html_minify(html_file.read())

                with open(i, 'w') as html_min_file:
                    min = html_min_file.write(min_html)


if __name__ == '__main__':
    print('Compiling index and work templates')
    compile_template('home.html', 'index')
    compile_template('work.html', 'work')

    print('Minifying css file')
    minify_css()

    print('Minifying html files')
    minify_html()

