from math import sin, cos, pi, acos
from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np

class transformation_3d(ABC):
    # @abstractmethod
    def to_css(self):
        pass 

    @abstractmethod
    def inverted(self):
        pass

    @abstractmethod
    def transform(self, point):
        pass

class rotation_3d(transformation_3d):
    angle_radians: float

    @abstractmethod
    def create_matrix(self):
        pass

    def transform(self, point):
        return np.matmul(self.create_matrix(), point)

@dataclass
class rotationX(rotation_3d):
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
    
@dataclass
class rotationY(rotation_3d):
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
    
@dataclass
class rotationZ(rotation_3d):
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