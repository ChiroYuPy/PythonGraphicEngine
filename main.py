from camera import Camera
from keys import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_Z, KEY_S, KEY_D, KEY_Q, KEY_W, KEY_A, KEY_ESCAPE
from app import App, Window
from color import Color
from components import Material, Mesh, Transform
from entity import Entity
from render_system import RenderSystem
from vector import Vector3

if __name__ == '__main__':
    window = Window()

    app = App(max_fps=330)

    mesh = Mesh([(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
                 (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)])

    cube_material = Material(diffuse=[1.0, 0.0, 0.0, 1.0], shininess=[50.0])

    transform = Transform(Vector3(0, 1, 0))

    cube_entity = Entity()
    cube_entity.add_component(cube_material)
    cube_entity.add_component(mesh)
    cube_entity.add_component(transform)

    camera = Camera(Vector3(0, 0, -10), Vector3(5, 0, 0), 90, window.width/window.height)

    render_system = RenderSystem(window, camera)

    black = Color(0, 0, 0)

    keys_pressed = set()
    camera_movement_speed = 10
    camera_rotation_speed = 100

    @app.event
    def update(dt):
        transform = cube_entity.get_component(Transform)
        transform.position.x += dt

        if KEY_DOWN in keys_pressed:
            camera.position.z += - camera_movement_speed * dt
        if KEY_UP in keys_pressed:
            camera.position.z += camera_movement_speed * dt
        if KEY_LEFT in keys_pressed:
            camera.position.x += - camera_movement_speed * dt
        if KEY_RIGHT in keys_pressed:
            camera.position.x += camera_movement_speed * dt

        if KEY_S in keys_pressed:
            camera.rotation.x += - camera_rotation_speed * dt
        if KEY_W in keys_pressed:
            camera.rotation.x +=  camera_rotation_speed * dt
        if KEY_D in keys_pressed:
            camera.rotation.y += - camera_rotation_speed * dt
        if KEY_A in keys_pressed:
            camera.rotation.y += camera_rotation_speed * dt

    @app.event
    def fixed_update(fixed_dt):
        pass
        # print(1/fixed_dt)

    @window.event
    def on_draw():
        window.clear(black)
        render_system.render(Entity.entities)

    @window.event
    def on_mouse_press(button):
        print(button, "window1")
        if button == 0:
            window.set_mouse_active(False)

    @window.event
    def on_mouse_move(x, y, dx, dy):
        print(x, y)
        if not window.get_mouse_active():
            camera.rotation.y += dx * 0.1
            camera.rotation.x += dy * 0.1

    @window.event
    def on_window_close():
        window.close()
        print("Window 1 is closing")

    @window.event
    def on_window_resize(width, height):
        print(f"Window 1 resized to {width}x{height}")

    @window.event
    def on_window_focus():
        print("Window 1 gained focus")

    @window.event
    def on_window_unfocus():
        print("Window 1 lost focus")

    @window.event
    def on_key_press(key, mods):
        print(f"Key pressed in Window 1: {key}")
        keys_pressed.add(key)
        if key == KEY_ESCAPE:
            window.set_mouse_active(True)

    @window.event
    def on_key_release(key, mods):
        print(f"Key released in Window 1: {key}")
        keys_pressed.remove(key)

    @window.event
    def on_window_iconify():
        print("Window 1 was iconified")

    @window.event
    def on_window_maximize():
        print("Window 1 was maximized")

    @window.event
    def on_window_restore():
        print("Window 1 was restored")

    @window.event
    def on_key_repeat(key, mods):
        print(f"Key repeated in Window 1: {key}")

    app.run()
