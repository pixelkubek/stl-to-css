from dataclasses import dataclass
from math import sin, cos, pi, acos

import numpy as np
from numpy import linalg as LA

from triangle3d import triangle_3d, align_p1_p2_p3
from html import html_css_of_triangle

my_trig = triangle_3d([
    np.array([0, -40, 0]).reshape(-1, 1),
    np.array([40, 0, 0]).reshape(-1, 1),
    np.array([0, 0, 40]).reshape(-1, 1)
])


triangle, transformations = align_p1_p2_p3(my_trig)

html, css = html_css_of_triangle(triangle, transformations, "face1", 5)


print(html)
print(css)
print(transformations)

