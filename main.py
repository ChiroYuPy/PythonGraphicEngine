from random import randint

from camera import Camera
from keys import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_Z, KEY_S, KEY_D, KEY_Q, KEY_W, KEY_A, KEY_ESCAPE, \
    KEY_LEFT_SHIFT, KEY_SPACE
from app import App, Window
from color import Color
from components import Material, Mesh, Transform, RigidBody
from entity import Entity
from physic_system import PhysicSystem
from render_system import RenderSystem
from vector import Vector3

if __name__ == '__main__':
    window = Window(width=1280, height=720)
    window.set_position(window.width/2, window.height/2)

    app = App(max_fps=330)

    mesh = Mesh([(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
                 (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)])

    cube_material = Material(diffuse=[1.0, 0.0, 0.0, 1.0], shininess=[50.0])

    entities = []
    for x in range(-2, 3):
        for z in range(-2, 3):
            cube_entity = Entity()
            entities.append(cube_entity)
            cube_entity.add_component(cube_material)
            cube_entity.add_component(RigidBody())
            cube_entity.add_component(mesh)
            cube_entity.add_component(Transform(Vector3(randint(-1, 1)/10, randint(5, 10), randint(-1, 1)/10)))

    camera = Camera(Vector3(0, -5, -10), Vector3(0, 0, 0), 90, window.width/window.height)

    render_system = RenderSystem(window)
    physic_system = PhysicSystem()

    black = Color(0, 0, 0)

    keys_pressed = set()
    camera_movement_speed = 10

    @app.event
    def update(dt):

        if KEY_S in keys_pressed:
            camera.position.z -= camera_movement_speed * dt
        if KEY_W in keys_pressed:
            camera.position.z += camera_movement_speed * dt
        if KEY_D in keys_pressed:
            camera.position.x -= camera_movement_speed * dt
        if KEY_A in keys_pressed:
            camera.position.x += camera_movement_speed * dt
        if KEY_SPACE in keys_pressed:
            camera.position.y -= camera_movement_speed * dt
        if KEY_LEFT_SHIFT in keys_pressed:
            camera.position.y += camera_movement_speed * dt

    @app.event
    def fixed_update(fixed_dt):
        physic_system.step(Entity.entities, fixed_dt)

    @window.event
    def on_draw():
        window.clear(black)
        render_system.render(Entity.entities)

    @window.event
    def on_mouse_press(button):
        if button == 0:
            window.set_mouse_active(False)

    @window.event
    def on_mouse_move(x, y, dx, dy):
        if not window.get_mouse_active():
            camera.rotation.y += dx * 0.1
            camera.rotation.x += dy * 0.1

    @window.event
    def on_window_close():
        window.close()

    @window.event
    def on_key_press(key, mods):
        keys_pressed.add(key)
        if key == KEY_ESCAPE:
            window.set_mouse_active(True)

    @window.event
    def on_key_release(key, mods):
        keys_pressed.remove(key)

    app.run()
