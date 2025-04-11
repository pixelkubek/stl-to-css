from dataclasses import dataclass
from math import sin, cos, pi, acos

import numpy as np
from numpy import linalg as LA

from triangle3d import triangle_3d
from html import html_css_of_object3d
from object3d import object_3d

my_trig = triangle_3d(
    [0, -22500, 0],
    [22500, 0, 0],
    [0, 0, 22500]
)

my_trig2 = triangle_3d(
    [0, -22500, 0],
    [-22500, 0, 0],
    [0, 0, 22500]
)

my_trig3 = triangle_3d(
    [0, 22500, 0],
    [-22500, 0, 0],
    [0, 0, 22500]
)

my_trig4 = triangle_3d(
    [0, 22500, 0],
    [22500, 0, 0],
    [0, 0, 22500]
)

my_trig5 = triangle_3d(
    [0, -22500, 0],
    [22500, 0, 0],
    [0, 0, -22500]
)

my_trig6 = triangle_3d(
    [0, -22500, 0],
    [-22500, 0, 0],
    [0, 0, -22500]
)

my_trig7 = triangle_3d(
    [0, 22500, 0],
    [-22500, 0, 0],
    [0, 0, -22500]
)

my_trig8 = triangle_3d(
    [0, 22500, 0],
    [22500, 0, 0],
    [0, 0, -22500]
)


obj = object_3d([my_trig, my_trig2, my_trig3, my_trig4, my_trig5, my_trig6, my_trig7, my_trig8])

obj.fit_to_size(500)

html, css = html_css_of_object3d(obj, "obj1", 500)


print(html)
print(css)

