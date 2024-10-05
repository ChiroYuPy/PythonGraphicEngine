from components import Transform, Component
from vector import Vector3


class Entity:
    entities = []

    def __init__(self):
        self.components = {}
        self.add_entity(self)
        self.add_transform()

    def add_component(self, component: Component):
        self.components[component.__class__.__name__] = component

    def get_component(self, component_name: str) -> Component:
        return self.components[component_name.__class__.__name__]

    def try_has_component(self, component_name: str):
        return component_name in self.components

    def add_transform(self):
        transform = Transform(position=Vector3(0, 0, 0), rotation=Vector3(0, 0, 0), scale=Vector3(0, 0, 0))
        self.add_component(transform)

    def delete(self):
        self.components.clear()

    def update(self, dt):
        pass

    @staticmethod
    def add_entity(entity):
        Entity.entities.append(entity)

    @staticmethod
    def remove_entity(entity):
        entity.delete()
        Entity.entities.remove(entity)
