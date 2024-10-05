from app import App, Window
from color import Color
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

    black = Color(0, 0, 0)

    @app.event
    def update(dt):
        pass
        # print(1/dt)

    @app.event
    def fixed_update(fixed_dt):
        pass
        # print(1/fixed_dt)

    @window.event
    def on_draw():
        window.clear(black)

    @window.event
    def on_mouse_press(button):
        print(button, "window1")

    @window.event
    def on_mouse_move(x, y):
        print(x, y)

    @window.event
    def on_window_close():
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

    @window.event
    def on_key_release(key, mods):
        print(f"Key released in Window 1: {key}")

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

    @window2.event
    def on_mouse_press(button):
        print(button, "window2")

    @window2.event
    def on_window_close():
        print("Window 2 is closing")

    @window2.event
    def on_window_resize(width, height):
        print(f"Window 2 resized to {width}x{height}")

    @window2.event
    def on_window_focus():
        print("Window 2 gained focus")

    @window2.event
    def on_window_unfocus():
        print("Window 2 lost focus")

    @window2.event
    def on_key_press(key, mods):
        print(f"Key pressed in Window 2: {key}")

    @window2.event
    def on_key_release(key, mods):
        print(f"Key released in Window 2: {key}")

    @window2.event
    def on_window_iconify():
        print("Window 2 was iconified")

    @window2.event
    def on_window_maximize():
        print("Window 2 was maximized")

    @window2.event
    def on_window_restore():
        print("Window 2 was restored")

    @window2.event
    def on_key_repeat(key, mods):
        print(f"Key repeated in Window 2: {key}")

    app.run()
