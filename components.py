from vector import Vector3


class Component:
    pass


class Transform(Component):
    def __init__(self, position: Vector3, rotation: Vector3 = Vector3(), scale: Vector3 = Vector3()):
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


class RigidBody(Component):
    def __init__(self, linear_velocity: Vector3 = Vector3(),
                 acceleration: Vector3 = Vector3(),
                 angular_velocity: Vector3 = Vector3(),
                 mass=1, friction=1, elasticity=1):

        self.linear_velocity = linear_velocity
        self.acceleration = acceleration
        self.angular_velocity = angular_velocity
        self.mass = mass
        self.friction = friction
        self.elasticity = elasticity


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