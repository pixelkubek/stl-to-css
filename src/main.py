from dataclasses import dataclass
from math import sin, cos, pi, acos

import numpy as np
from numpy import linalg as LA

from triangle3d import triangle_3d
from html import html_css_of_object3d
from object3d import object_3d

my_trig = triangle_3d(
    [0, -225, 0],
    [225, 0, 0],
    [0, 0, 225]
)

my_trig2 = triangle_3d(
    [0, -225, 0],
    [-225, 0, 0],
    [0, 0, 225]
)

my_trig3 = triangle_3d(
    [0, 225, 0],
    [-225, 0, 0],
    [0, 0, 225]
)

my_trig4 = triangle_3d(
    [0, 225, 0],
    [225, 0, 0],
    [0, 0, 225]
)

obj = object_3d([my_trig, my_trig2, my_trig3, my_trig4])

html, css = html_css_of_object3d(obj, "obj1", 500)


print(html)
print(css)

