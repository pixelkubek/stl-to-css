from math import sin, cos, pi, acos

import numpy as np

class transformation_3d:
    def to_css(self):
        pass 

    def inverted(self):
        pass


class rotationX(transformation_3d):
    angle_radians: float

    def __init__(self, angle_radians):
        self.angle_radians = angle_radians

    def inverted(self):
        return rotationX(-self.angle_radians)
    
    def create_matrix(self):
        return np.array([
            [1, 0, 0],
            [0, cos(self.angle_radians), -sin(self.angle_radians)],
            [0, sin(self.angle_radians), cos(self.angle_radians)]
        ])
    
class rotationY(transformation_3d):
    angle_radians: float

    def __init__(self, angle_radians):
        self.angle_radians = angle_radians

    def inverted(self):
        return rotationY(-self.angle_radians)
    
    def create_matrix(self):
        return np.array([
            [cos(self.angle_radians), 0, sin(self.angle_radians)],
            [0, 1, 0],
            [-sin(self.angle_radians), 0, cos(self.angle_radians)]
        ])
    
class rotationZ(transformation_3d):
    angle_radians: float

    def __init__(self, angle_radians):
        self.angle_radians = angle_radians

    def inverted(self):
        return rotationZ(-self.angle_radians)
    
    def create_matrix(self):
        return np.array([
            [cos(self.angle_radians), -sin(self.angle_radians), 0],
            [sin(self.angle_radians), cos(self.angle_radians), 0],
            [0, 0, 1]
        ])