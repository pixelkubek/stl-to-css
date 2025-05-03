from argparse import ArgumentParser

from html import html_css_of_object3d
from object3d import read_stl_file

if __name__ == '__main__':
    parser = ArgumentParser(description="Convert an stl file to html and css files")
    parser.add_argument("-i", "--input", type=str, help="Stl file to read", required=True)
    parser.add_argument("-o", "--htmlfile", type=str, help="Html output destination file")
    parser.add_argument("-c", "--cssfile", type=str, help="Css output destination file")
    parser.add_argument("-f", "--file", type=str, help="Combined output destination file")
    parser.add_argument("-d", "--display", action="store_true", help="Print combined output to stdout", default=False)
    parser.add_argument("-s", "--size", type=int, help="Desired html element size", required=True)
    parser.add_argument("-u", "--unit", type=str, help="Html unit used", default='px')
    parser.add_argument("--color", type=str, help="3d object face color in css notation", default='red')
    parser.add_argument("--svg_pixel_scale", type=int, help="How many size units are in an svg pixel, controls contour length", default=1)

    args = parser.parse_args()

    obj = read_stl_file(args.input)
    obj.fit_to_size(args.size)
    html, css = html_css_of_object3d(obj, args.size, svg_pixel_scale = args.svg_pixel_scale, color=args.color, unit=args.unit)

    if args.htmlfile is not None:
        with open(args.htmlfile, 'w') as f:
            print(html, file=f)

    if args.cssfile is not None:
        with open(args.cssfile, 'w') as f:
            print(html, file=f)

    combined = f'''<!DOCTYPE html>
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
'''
    if args.display:
        print(combined)

    if args.file is not None:
        with open(args.file, 'w') as f:
            print(combined, file=f)