import inspect
import glfw
from OpenGL.raw.GL.VERSION.GL_1_0 import glClearColor, glClear, GL_COLOR_BUFFER_BIT


class Window:
    windows = []

    def __init__(self, width=800, height=600, title="Graphic Engine « ChiroYuPy » - v.0.0.1"):
        self.width = width
        self.height = height
        self.title = title

        self.events = {}

        self.add_window(self)

        def error_callback(window, error):
            print(error)

        if not glfw.init():
            raise Exception("Error initializing glfw")

        glfw.set_error_callback(error_callback)

        self.glfw_window = glfw.create_window(self.width, self.height, self.title, None, None)

        if not self.glfw_window:
            glfw.terminate()
            raise Exception("glfw window creation failed")

    def clear(self):
        print(f"{self.__class__.__name__} cleared")

    def event(self, func):
        num_params = len(inspect.signature(func).parameters)

        if func.__name__ == 'on_draw' and num_params != 0:
            raise ValueError("The 'on_draw' event handler must accept exactly 0 parameters.")

        self.events[func.__name__] = func
        return func

    def update(self):
        if glfw.get_window_attrib(self.glfw_window, glfw.VISIBLE):
            glfw.make_context_current(self.glfw_window)
            glClearColor(1.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.glfw_window)
            glfw.poll_events()
            if 'on_draw' in self.events:
                self.events['on_draw']()

    @staticmethod
    def add_window(window):
        Window.windows.append(window)