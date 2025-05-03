from math import sin, cos, pi, acos
from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np

class transformation_3d(ABC):
    @abstractmethod
    def to_css(self, unit: str = 'px'):
        return '{}' 

    @abstractmethod
    def inverted(self):
        pass

    @abstractmethod
    def transform(self, point):
        pass

@dataclass
class translate_3d(transformation_3d):
    x: float
    y: float
    z: float

    def inverted(self):
        return translate_3d(-self.x, -self.y, -self.z)
    
    def transform(self, point):
        return point + np.array([self.x, self.y, self.z]).reshape(-1, 1)
    
    def to_css(self, unit: str = 'px'):
        # y direction is swapped in css
        return f'transform: translate3d({self.x}{unit},{self.z}{unit},{-self.y}{unit});' 

@dataclass
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
        super().__init__(angle_radians)

    def inverted(self):
        return rotationX(-self.angle_radians)
    
    def create_matrix(self):
        return np.array([
            [1, 0, 0],
            [0, cos(self.angle_radians), -sin(self.angle_radians)],
            [0, sin(self.angle_radians), cos(self.angle_radians)]
        ])
    
    def to_css(self, unit: str = 'px'):
        return f'transform: rotateX({self.angle_radians}rad);' 
    
@dataclass
class rotationY(rotation_3d):
    def __init__(self, angle_radians):
        super().__init__(angle_radians)

    def inverted(self):
        return rotationY(-self.angle_radians)
    
    def create_matrix(self):
        return np.array([
            [cos(self.angle_radians), 0, sin(self.angle_radians)],
            [0, 1, 0],
            [-sin(self.angle_radians), 0, cos(self.angle_radians)]
        ])

    def to_css(self, unit: str = 'px'):
        # css has different axis names for y and z
        return f'transform: rotateZ({-self.angle_radians}rad);' 
    
@dataclass
class rotationZ(rotation_3d):
    def __init__(self, angle_radians):
        super().__init__(angle_radians)

    def inverted(self):
        return rotationZ(-self.angle_radians)
    
    def create_matrix(self):
        return np.array([
            [cos(self.angle_radians), -sin(self.angle_radians), 0],
            [sin(self.angle_radians), cos(self.angle_radians), 0],
            [0, 0, 1]
        ])

    def to_css(self, unit: str = 'px'):
        # css has different axis names for y and z
        return f'transform: rotateY({self.angle_radians}rad);' 