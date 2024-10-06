from components import Transform, RigidBody
from vector import Vector3


class Collision:
    @staticmethod
    def collide(center_a, radius_a, center_b, radius_b):
        collision = True
        normal = Vector3()
        depth = 0.0

        distance = Vector3.distance(center_a, center_b)
        radii = radius_a + radius_b

        if distance >= radii:
            collision = False
        else:
            normal = Vector3.normalize(center_b - center_a)
            depth = radii - distance

        return collision, normal, depth


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class PhysicSystem:
    def __init__(self):
        self.gravity = Vector3(0, -9.81, 0)
        self.contact_pairs = []

    def step(self, entities, dt):
        self.update(entities, dt)
        self.broad_phase(len(entities))
        self.narrow_phase(entities, dt)

    def update(self, entities, dt):
        for entity in entities:
            transform = entity.get_component(Transform)
            rigid_body = entity.get_component(RigidBody)

            rigid_body.linear_velocity += self.gravity * dt

            transform.position += rigid_body.linear_velocity * dt

            if transform.position.y <= 0:
                transform.position.y = 0
                rigid_body.linear_velocity *= -0.9

    def broad_phase(self, entities_count):
        self.contact_pairs.clear()
        for i in range(entities_count - 1):
            for j in range(i + 1, entities_count):
                self.contact_pairs.append(Pair(i, j))

    def narrow_phase(self, entities, pairs):
        for pair in self.contact_pairs:
            bodyA = entities[pair.a]
            bodyB = entities[pair.b]

            bodyA_transform = bodyA.get_component(Transform)
            bodyB_transform = bodyB.get_component(Transform)

            bodyA_rigid_body = bodyA.get_component(RigidBody)
            bodyB_rigid_body = bodyB.get_component(RigidBody)

            collide, normal, depth = Collision.collide(bodyA_transform.position, 1, bodyB_transform.position, 1)

            if collide:
                self.separate_bodies(bodyA_transform, bodyB_transform, normal*depth*2)


    @staticmethod
    def separate_bodies(transformA, transformB, mtv):
        transformA.position -= mtv / 2
        transformB.position += mtv / 2