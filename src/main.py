from triangle3d import triangle_3d
from html import html_css_of_object3d
from object3d import object_3d, object_from_ascii_stl

import sys
# my_trig = triangle_3d(
#     [0, -22500, 0],
#     [22500, 0, 0],
#     [0, 0, 22500]
# )

# my_trig2 = triangle_3d(
#     [0, -22500, 0],
#     [-22500, 0, 0],
#     [0, 0, 22500]
# )

# my_trig3 = triangle_3d(
#     [0, 22500, 0],
#     [-22500, 0, 0],
#     [0, 0, 22500]
# )

# my_trig4 = triangle_3d(
#     [0, 22500, 0],
#     [22500, 0, 0],
#     [0, 0, 22500]
# )

# my_trig5 = triangle_3d(
#     [0, -22500, 0],
#     [22500, 0, 0],
#     [0, 0, -22500]
# )

# my_trig6 = triangle_3d(
#     [0, -22500, 0],
#     [-22500, 0, 0],
#     [0, 0, -22500]
# )

# my_trig7 = triangle_3d(
#     [0, 22500, 0],
#     [-22500, 0, 0],
#     [0, 0, -22500]
# )

# my_trig8 = triangle_3d(
#     [0, 22500, 0],
#     [22500, 0, 0],
#     [0, 0, -22500]
# )


# obj = object_3d([my_trig, my_trig2, my_trig3, my_trig4, my_trig5, my_trig6, my_trig7, my_trig8], 'obj1')

# obj.fit_to_size(500)

# html, css = html_css_of_object3d(obj, 500)

# print(f'''<!DOCTYPE html>
# <html>
#     <head>
#         <link rel="stylesheet" href="test.css">
#         <style>
#             {css}
#         </style>
#     </head>
#     <body>
#         {html}
#     </body>
# </html>
# ''')

with open('pikachu.stl', 'r') as f:
    obj = object_from_ascii_stl(f)


obj.fit_to_size(500)

html, css = html_css_of_object3d(obj, 500)
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