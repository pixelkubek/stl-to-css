from dataclasses import dataclass
from math import sin, cos

import numpy as np

def create_x_rotation_matrix(angle_radians: float) -> np.ndarray:
    return np.array(
        [1, 0, 0],
        [0, cos(angle_radians), -sin(angle_radians)],
        [0, sin(angle_radians), cos(angle_radians)]
    )

def create_y_rotation_matrix(angle_radians: float) -> np.ndarray:
    return np.array(
        [cos(angle_radians), 0, sin(angle_radians)],
        [0, 1, 0],
        [-sin(angle_radians), 0, cos(angle_radians)]
    )

def create_z_rotation_matrix(angle_radians: float) -> np.ndarray:
    return np.array(
        [cos(angle_radians), -sin(angle_radians), 0],
        [sin(angle_radians), cos(angle_radians), 0],
        [0, 0, 1]
    )

@dataclass
class triangle_3d:
    vertices: tuple[np.ndarray, np.ndarray, np.ndarray]

    def origin_representation(self):
        p1, p2, p3 = self.vertices
        return triangle_3d(vertices=(p1 - p1, p2 - p1, p3 - p1))


my_trig = triangle_3d((
    np.array([0, 0, 0]),
    np.array([-100, 0, 0]),
    np.array([-50, -100, 0])
))

print(my_trig)