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
    parser.add_argument("-n", "--name", type=str, help="Object name and html id", default="obj")
    parser.add_argument("--add_example_animation", action="store_true", help="Add an animation to the css", default=False)

    args = parser.parse_args()

    obj = read_stl_file(args.input, object_name=args.name)
    obj.fit_to_size(args.size)
    html, css = html_css_of_object3d(obj, args.size, svg_pixel_scale = args.svg_pixel_scale, color=args.color, unit=args.unit)

    if args.add_example_animation:
        css += f'''
#{args.name} {{
    transform-origin: center;
    animation: spin_{args.name} 20s infinite ease-in-out;
}}

@keyframes spin_{args.name} {{
    0% {{
        transform: rotateY(0deg) rotateX(0deg) rotateZ(0deg);
    }}

    25% {{
        transform: rotateY(90deg) rotateX(180deg) rotateZ(360deg);

    }}

    50% {{
        transform: rotateY(180deg) rotateX(360deg);

    }}

    75% {{
        transform: rotateY(270deg) rotateX(180deg) rotateZ(0deg);
    }}

    100% {{
        transform: rotateY(360deg) rotateX(360deg)  rotateZ(360deg);

    }}
}}'''


    if args.htmlfile is not None:
        with open(args.htmlfile, 'w') as f:
            print(html, file=f)

    if args.cssfile is not None:
        with open(args.cssfile, 'w') as f:
            print(css, file=f)

    combined = f'''<!DOCTYPE html>
<html>
    <head>
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