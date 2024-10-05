from vector import Vector3


class Component:
    pass


class Transform(Component):
    def __init__(self, position: Vector3, rotation: Vector3, scale: Vector3):
        self.position = position
        self.rotation = rotation
        self.scale = scale


class Mesh(Component):
    def __init__(self, vertices):
        self.vertices = vertices


class Material(Component):
    def __init__(self, diffuse, shininess):
        self.diffuse = diffuse
        self.shininess = shininess


class Light(Component):
    def __init__(self, position, ambient, diffuse, specular):
        self.position = position
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular


class Camera(Component):
    def __init__(self, fov, render_distance):
        self.fov = fov
        self.render_distance = render_distance