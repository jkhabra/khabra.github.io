#!/usr/bin/env python3
from css_html_js_minify import css_minify, html_minify
from jinja2 import Environment, FileSystemLoader
from PIL import Image
import os

cwd = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(cwd, '__source/templates/')
static_dir = os.path.join(cwd, '__source/static/')
bundle_dir = os.path.join(cwd, 'bundle/')


def compile_template(template, name):
    dir_path = os.path.dirname(os.path.abspath('./portfolio'))
    env = Environment(loader=FileSystemLoader(os.path.join(dir_path, "__source/templates")))
    template = env.get_template(template)
    combine_html = template.render(data={'active_page': name})

    with open(os.path.join(cwd, name + '.html'), 'w') as f:
        combine = f.write(combine_html)

def minify_css():
    if not os.path.exists(bundle_dir):
        dir = os.path.dirname(bundle_dir)
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

def jpg_into_png(image):
    images_path = os.listdir(static_dir + 'images/')

    for i in images_path:
        if i.endswith('.jpg'):
            image = Image.open(static_dir+'images/'+i)
            print('converting {} into png'.format(i))
            image.convert('RGB').save(bundle_dir + '{}{}.png'.format('images/', i.split('.')[0]), 'PNG')

def image_compression():
    if not os.path.exists(bundle_dir + 'images/'):
        dir = os.path.dirname(bundle_dir + 'images/')
        os.makedirs(dir)

    images_path = os.listdir(static_dir + 'images/')
    #images_path = os.listdir(bundle_dir + 'images/')

    for i in images_path:
        if i.endswith('.jpg'):
            image = Image.open(static_dir + 'images/' + i)
            #image_sieze = image.size
            print('compressing {} '.format(i))
            image.save(bundle_dir + 'images/{}'.format(i),optimize=True,quality=75)

if __name__ == '__main__':
    print('Compiling index and work templates')
    compile_template('home.html', 'index')
    compile_template('work.html', 'work')

    print('Minifying css file')
    minify_css()

    print('Minifying html files')
    minify_html()

