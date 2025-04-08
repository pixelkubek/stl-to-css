from dataclasses import dataclass

@dataclass
class vector_3d:
    x: float
    y: float
    z: float

    def __add__(self, other):
        return vector_3d(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __sub__(self, other):
        return vector_3d(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

@dataclass
class triangle_3d:
    vertices: tuple[vector_3d, vector_3d, vector_3d]

    def origin_representation(self):
        p1, p2, p3 = self.vertices
        return triangle_3d(vertices=(p1 - p1, p2 - p1, p3 - p1))



