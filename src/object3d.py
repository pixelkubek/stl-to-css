from triangle3d import triangle_3d, align_p1_p2_p3, get_xyz
from transformations import transformation_3d, translate_3d

from numpy import linalg as LA

class object_3d:
    faces: list[triangle_3d]

    def __init__(self, faces):
        self.faces = faces

    def __str__(self):
        return f"object3d(faces={self.faces})"
    
    def transformed_faces(self) -> list[tuple[triangle_3d, list[transformation_3d]]]:
        return [align_p1_p2_p3(f) for f in self.faces]

    def fit_to_size(self, size):
        min_x, min_y, min_z = 0, 0, 0 

        for face in self.faces:
            for point in face.vertices:
                x, y, z = get_xyz(point)
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                min_z = min(min_z, z)
                print(z)

        transformation = translate_3d(-min_x, -min_y, -min_z)

        for face in self.faces:
            face.transform(transformation)
        print(self.faces)

        print(transformation)

        max_distance = 0

        for face in self.faces:
            for point in face.vertices:
                max_distance = max(max_distance, LA.norm(point))
                print(z)


        if max_distance != 0:
            for face in self.faces:
                for i in range(len(face.vertices)):
                    print(face.vertices[i] * size / (max_distance))
                    face.vertices[i] = face.vertices[i] * size / (max_distance)
