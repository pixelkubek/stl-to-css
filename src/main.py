from triangle3d import triangle_3d
from html import html_css_of_object3d
from object3d import object_3d, read_stl_file

import sys

if __name__ == '__main__':
    obj = read_stl_file('pikachu.stl', 'obj')
    obj.fit_to_size(50)

    html, css = html_css_of_object3d(obj, 50, svg_pixel_scale = 10, color='yellow', unit='vh')
    # print(obj, file=sys.stderr)

    print(f'''<!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="test.css">
            <style>
                {css}
            </style>
        </head>
        <body>
            {html}
        </body>
    </html>
    ''')