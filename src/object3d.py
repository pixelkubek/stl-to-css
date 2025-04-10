from triangle3d import triangle_3d, align_p1_p2_p3
from transformations import transformation_3d

class object_3d:
    faces: list[triangle_3d]

    def __init__(self, faces):
        self.faces = faces

    def __str__(self):
        return f"object3d(faces={self.faces})"
    
    def transformed_faces(self) -> list[tuple[triangle_3d, list[transformation_3d]]]:
        return [align_p1_p2_p3(f) for f in self.faces]