# STL-TO-CSS

Convert an stl file into a 3d html object comprising of `<div>` and `<svg>` elements.

The resulting object is compatible with css 3d animations and transformations.

## Dependencies
Virtual environment is recommended.

To install requirements run

```
pip install -r requirements.txt
```

## Usage
```
usage: main.py [-h] -i INPUT [-o HTMLFILE] [-c CSSFILE] [-f FILE] [-d] -s SIZE [-u UNIT] [--color COLOR] [--svg_pixel_scale SVG_PIXEL_SCALE] [-n NAME] [--add_example_animation]

Convert an stl file to html and css files

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Stl file to read
  -o HTMLFILE, --htmlfile HTMLFILE
                        Html output destination file
  -c CSSFILE, --cssfile CSSFILE
                        Css output destination file
  -f FILE, --file FILE  Combined output destination file
  -d, --display         Print combined output to stdout
  -s SIZE, --size SIZE  Desired html element size
  -u UNIT, --unit UNIT  Html unit used
  --color COLOR         3d object face color in css notation
  --svg_pixel_scale SVG_PIXEL_SCALE
                        How many size units are in an svg pixel, controls contour length
  -n NAME, --name NAME  Object name and html id
  --add_example_animation
                        Add an animation to the css
```