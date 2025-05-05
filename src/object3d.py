from triangle3d import triangle_3d, align_p1_p2_p3, get_xyz
from transformations import transformation_3d, translate_3d


from numpy import linalg as LA
import numpy as np
import struct
import sys

class object_3d:
    faces: list[triangle_3d]
    name: str

    def __init__(self, faces, name = 'object3d'):
        self.faces = faces
        self.name = name

    def __str__(self):
        return f"object3d(faces={self.faces})"
    
    # For each face, return it's triangle3d along with a list of transformations
    # to move it to the XZ plane with one side on the X axis.
    def transformed_faces(self) -> list[tuple[triangle_3d, list[transformation_3d]]]:
        return [align_p1_p2_p3(f) for f in self.faces]

    # Scale the object for all variables to be between 0 and size.
    def fit_to_size(self, size):
        min_x, min_y, min_z = 0, 0, 0 

        for face in self.faces:
            for point in face.vertices:
                x, y, z = get_xyz(point)
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                min_z = min(min_z, z)

        transformation = translate_3d(-min_x, -min_y, -min_z)

        for face in self.faces:
            face.transform(transformation)


        max_distance = 0

        for face in self.faces:
            for point in face.vertices:
                max_distance = max(max_distance, LA.norm(point))


        if max_distance != 0:
            for face in self.faces:
                for i in range(len(face.vertices)):
                    face.vertices[i] = face.vertices[i] * size / (max_distance)

    # Return a vector which moves the average point to the 0, 0, 0 coordinates.
    def center(self):
        sum_x, sum_y, sum_z = 0, 0, 0
        count = 0

        for face in self.faces:
            for point in face.vertices:
                x, y, z = get_xyz(point)
                sum_x += x
                sum_y += y
                sum_z += z
                count += 1
        
        return np.array([(sum_x / count), (sum_y / count), (sum_z / count)]).reshape(-1, 1)

# Given data representing the byte contents of a ascii stl file, return it's 3d object.
def object_from_ascii_stl(data, object_name: str):
    lines = data.splitlines()

    assert(lines[0].startswith(b'solid '))

    faces = []

    i = 1
    while lines[i].lstrip().startswith(b"facet"):
        i += 1 # ignore facet line
        assert(lines[i].strip() == b"outer loop")
        i += 1 # move to first vertex line

        points = []
        for _ in range(3):
            coordinates = []
            line = lines[i].strip()
            elements = line.split()
            assert(elements[0] ==  b"vertex")

            for j in range(3):
                coordinates.append(float(elements[j + 1]))

            coordinates[2] *= -1
            points.append(coordinates)
        
            i += 1

        assert(lines[i].strip() == b"endloop")
        i += 1

        assert(lines[i].strip() == b"endfacet")
        i += 1

        faces.append(triangle_3d(*points))

    return object_3d(faces, object_name)

    
# Given data representing the byte contents of a binary stl file, return it's 3d object.
def object_from_binary_stl(data, objest_name):
    index = 80 # skip header

    number_of_triangles, = struct.unpack('<I', data[index:index + 4])

    index += 4

    faces = []

    for _ in range(number_of_triangles):
        normal_x, normal_y, normal_z = struct.unpack("<fff", data[index: index + 12])
        index += 12

        points = []
        for _ in range(3):
            x, y, z = struct.unpack("<fff", data[index: index + 12])
            index += 12

            points.append([x, y, -z])
        
        faces.append(triangle_3d(*points))
        index += 2

    return object_3d(faces, objest_name)


def read_stl_file(pathname: str, object_name: str = 'obj') -> object_3d:
    with open(pathname, 'rb') as f:
        data = f.read()

        if data.startswith(b'solid'):
            return object_from_ascii_stl(data, object_name)
        else:
            return object_from_binary_stl(data, object_name)