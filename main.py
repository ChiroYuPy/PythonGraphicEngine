from app import App, Window
from components import Material, Mesh
from entity import Entity
from vector import Vector3

if __name__ == '__main__':
    window = Window()
    window2 = Window()
    app = App()

    mesh = Mesh([Vector3(-0.5, -0.5, -0.5), Vector3(0.5, -0.5, -0.5), Vector3(0.5, 0.5, -0.5), Vector3(-0.5, 0.5, -0.5),
                 Vector3(-0.5, -0.5, 0.5), Vector3(0.5, -0.5, 0.5), Vector3(0.5, 0.5, 0.5), Vector3(-0.5, 0.5, 0.5)])

    cube_material = Material(diffuse=[1.0, 0.0, 0.0, 1.0], shininess=[50.0])

    cube_entity = Entity()
    cube_entity.add_component(cube_material)
    cube_entity.add_component(mesh)

    @app.event
    def update(dt):
        print(1/dt)

    @app.event
    def fixed_update(fixed_dt):
        print(1/fixed_dt)

    @window.event
    def on_draw():
        window.clear()

    app.run()