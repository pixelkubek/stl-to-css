from dataclasses import dataclass
from math import sin, cos, pi, acos

import numpy as np
from numpy import linalg as LA

def create_x_rotation_matrix(angle_radians: float) -> np.ndarray:
    return np.array([
        [1, 0, 0],
        [0, cos(angle_radians), -sin(angle_radians)],
        [0, sin(angle_radians), cos(angle_radians)]
    ])

def create_y_rotation_matrix(angle_radians: float) -> np.ndarray:
    return np.array([
        [cos(angle_radians), 0, sin(angle_radians)],
        [0, 1, 0],
        [-sin(angle_radians), 0, cos(angle_radians)]
    ])

def create_z_rotation_matrix(angle_radians: float) -> np.ndarray:
    return np.array([
        [cos(angle_radians), -sin(angle_radians), 0],
        [sin(angle_radians), cos(angle_radians), 0],
        [0, 0, 1]
    ])

def sgn(x: float):
    if x < 0:
        return -1
    else:
        return 1

@dataclass
class triangle_3d:
    vertices: list[np.ndarray]
    
    def apply_matrix_left(self, matrix):
        return triangle_3d([np.matmul(matrix, v) for v in self.vertices])

    def apply_matrix_right(self, matrix):
        return triangle_3d([np.matmul(v, matrix) for v in self.vertices])

    def origin_representation(self):
        # move p1 to [0, 0, 0]
        p1, p2, p3 = self.vertices
        p1, p2, p3 = p1 - p1, p2 - p1, p3 - p1

        polar_angle = acos(p2[2, 0] / LA.norm(p2))
        angle_of_rotation = sgn(p2[1, 0]) * acos(p2[0, 0] / LA.norm(p2[:2, 0]))
        print(polar_angle / pi * 180, angle_of_rotation / pi * 180)
        return 

# Moves triangle so that p1 has coordinates [0, 0, 0]
def align_p1(triangle: triangle_3d) -> triangle_3d:
    p1, p2, p3 = triangle.vertices
    return triangle_3d([p1 - p1, p2 - p1, p3 - p1])

def align_p1_p2(triangle: triangle_3d) -> triangle_3d:
    p1, p2, p3 = align_p1(triangle).vertices
    polar_angle = acos(p2[2, 0] / LA.norm(p2))
    angle_of_rotation = sgn(p2[1, 0]) * acos(p2[0, 0] / LA.norm(p2[:2, 0]))
    print(polar_angle / pi * 180, angle_of_rotation / pi * 180)

    return triangle_3d([
        p1,
        np.matmul(create_y_rotation_matrix(pi/2 - polar_angle), np.matmul(create_z_rotation_matrix(-angle_of_rotation), p2)),
        np.matmul(create_y_rotation_matrix(pi/2 - polar_angle), np.matmul(create_z_rotation_matrix(-angle_of_rotation), p3))
    ])

def align_p1_p2_p3(triangle: triangle_3d) -> triangle_3d:
    p1, p2, p3 = align_p1_p2(triangle).vertices
    
    projected_p3 = p3[1:3, 0] # p3 projected to yz plane
    up_vector = np.array([0, 1]).reshape(-1, 1)

    angle = acos(np.dot(projected_p3, up_vector).item() / (LA.norm(projected_p3) * LA.norm(up_vector)))

    print(angle)

    return triangle_3d([
        p1,
        p2,
        np.matmul(create_x_rotation_matrix(-angle), p3)
    ])

my_trig = triangle_3d([
    np.array([-300, 100, 100]).reshape(-1, 1),
    np.array([-300, 200, 100]).reshape(-1, 1),
    np.array([-300, 150, 50]).reshape(-1, 1)
])

print(align_p1_p2_p3(my_trig))