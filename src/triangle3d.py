from dataclasses import dataclass
from math import pi, acos, asin, sin

import numpy as np
from numpy import linalg as LA

from transformations import translate_3d, rotationX, rotationY, rotationZ, transformation_3d

def sgn(x: float):
    if x < 0:
        return -1
    else:
        return 1

def get_xyz(point):
    return point.ravel()

@dataclass
class triangle_3d:
    vertices: list[np.ndarray]

    def __init__(self, p1, p2, p3):
        self.vertices = [
            np.array(p1).reshape(-1, 1),
            np.array(p2).reshape(-1, 1),
            np.array(p3).reshape(-1, 1)
        ]
    
    def transform(self, transformation: transformation_3d):
        self.vertices = [transformation.transform(p) for p in self.vertices]


# Moves triangle so that p1 has coordinates [0, 0, 0]
def align_p1(triangle: triangle_3d) -> tuple[triangle_3d, list[transformation_3d]]:
    translation_3d = translate_3d(*get_xyz(triangle.vertices[0]))

    triangle.transform(translation_3d)

    return triangle, [translation_3d]

# Rotates triangle so that p1 has coordinates [0, 0, 0] and p2 is on the positive x axis
def align_p2(triangle: triangle_3d) -> tuple[triangle_3d, list[transformation_3d]]:
    _, p2, _ = triangle.vertices
    polar_angle = acos(p2[2, 0] / LA.norm(p2))
    angle_of_rotation = sgn(p2[1, 0]) * acos(p2[0, 0] / LA.norm(p2[:2, 0]))
    print(polar_angle / pi * 180, angle_of_rotation / pi * 180)

    print("z rotate: ", -angle_of_rotation)
    print("y rotate: ", pi/2 - polar_angle)

    z_rotation = rotationZ(-angle_of_rotation)
    y_rotation = rotationY(pi/2 - polar_angle)

    triangle.transform(z_rotation)

    # print(triangle)

    triangle.transform(y_rotation)

    return triangle, [z_rotation, y_rotation]

def align_p3(triangle: triangle_3d) -> tuple[triangle_3d, list[transformation_3d]]:
    _, _, p3 = triangle.vertices
    
    projected_p3 = p3[1:3, 0] # p3 projected to yz plane

    print(projected_p3)
    up_vector = np.array([0, 1]).reshape(-1, 1)

    # angle = acos(np.dot(projected_p3, up_vector).item() / (LA.norm(projected_p3) * LA.norm(up_vector)))
    angle = sgn(projected_p3[0]) * acos(projected_p3[1] / LA.norm(projected_p3))

    print(angle, angle / pi * 180)
    print("x rotate: ", angle)

    x_rotation = rotationX(angle)

    triangle.transform(x_rotation)
    print(triangle)

    return triangle, [x_rotation]

def align_p1_p2_p3(triangle: triangle_3d) -> tuple[triangle_3d, list[transformation_3d]]:
    all_transformations = []
    print("0: ", triangle)
    triangle, tansformations = align_p1(triangle)
    all_transformations.extend(tansformations)
    print("1: ", triangle)

    triangle, tansformations = align_p2(triangle)
    all_transformations.extend(tansformations)    
    print("2: ", triangle)
    
    triangle, tansformations = align_p3(triangle)
    all_transformations.extend(tansformations)
    print("3: ", triangle)
    return triangle, all_transformations
