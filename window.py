import inspect
from enum import Enum
import glfw
from OpenGL.raw.GL.VERSION.GL_1_0 import glClearColor, glClear, GL_COLOR_BUFFER_BIT
from color import Color


class Event(Enum):
    ON_DRAW = 'on_draw'
    ON_MOUSE_PRESS = 'on_mouse_press'
    ON_MOUSE_RELEASE = 'on_mouse_release'
    ON_MOUSE_MOVE = 'on_mouse_move'
    ON_WINDOW_CLOSE = 'on_window_close'
    ON_WINDOW_RESIZE = 'on_window_resize'
    ON_WINDOW_FOCUS = 'on_window_focus'
    ON_WINDOW_UNFOCUS = 'on_window_unfocus'
    ON_KEY_PRESS = 'on_key_press'
    ON_KEY_RELEASE = 'on_key_release'
    ON_WINDOW_ICONIFY = 'on_window_iconify'  # New event
    ON_WINDOW_MAXIMIZE = 'on_window_maximize'  # New event
    ON_WINDOW_RESTORE = 'on_window_restore'  # New event
    ON_KEY_REPEAT = 'on_key_repeat'  # New event


class Window:
    windows = []

    def __init__(self, width=800, height=600, title="Graphic Engine « ChiroYuPy » - v.0.0.1",
                 frame=True, resizeable=False, visible=True, floating=False, auto_iconify=False, maximize=False):

        self.width = width
        self.height = height
        self.title = title

        self.frame = frame
        self.resizeable = resizeable
        self.visible = visible
        self.floating = floating
        self.auto_iconify = auto_iconify
        self.maximize = maximize

        self.glfw_window = None
        self.events = {}
        self.init_glfw()

    def init_glfw(self):
        if not glfw.init():
            raise Exception("Error initializing GLFW")

        glfw.window_hint(glfw.DECORATED, glfw.TRUE if self.frame is True else glfw.FALSE)
        glfw.window_hint(glfw.RESIZABLE, glfw.TRUE if self.resizeable is True else glfw.FALSE)
        glfw.window_hint(glfw.VISIBLE, glfw.TRUE if self.visible is True else glfw.FALSE)
        glfw.window_hint(glfw.FLOATING, glfw.TRUE if self.floating is True else glfw.FALSE)
        glfw.window_hint(glfw.AUTO_ICONIFY, glfw.TRUE if self.auto_iconify is True else glfw.FALSE)
        glfw.window_hint(glfw.MAXIMIZED, glfw.TRUE if self.maximize is True else glfw.FALSE)

        self.glfw_window = glfw.create_window(self.width, self.height, self.title, None, None)
        if not self.glfw_window:
            glfw.terminate()
            raise Exception("Failed to create GLFW window")

        glfw.make_context_current(self.glfw_window)

        # Setup event callbacks
        glfw.set_window_user_pointer(self.glfw_window, self)

        glfw.set_mouse_button_callback(self.glfw_window, self.mouse_button_callback)
        glfw.set_cursor_pos_callback(self.glfw_window, self.cursor_position_callback)
        glfw.set_window_close_callback(self.glfw_window, self.window_close_callback)
        glfw.set_window_size_callback(self.glfw_window, self.window_size_callback)
        glfw.set_window_focus_callback(self.glfw_window, self.window_focus_callback)
        glfw.set_window_iconify_callback(self.glfw_window, self.window_iconify_callback)
        glfw.set_window_maximize_callback(self.glfw_window, self.window_maximize_callback)
        glfw.set_key_callback(self.glfw_window, self.key_callback)

        self.add_window(self)

    def clear(self, color=Color(0.0, 0.0, 0.0, 1.0)):
        glClearColor(color.r, color.g, color.b, color.a)
        glClear(GL_COLOR_BUFFER_BIT)

    def close(self):
        print(f"{self.__class__.__name__} is closing")
        glfw.destroy_window(self.glfw_window)
        glfw.terminate()

    def set_position(self, x, y):
        glfw.set_window_pos(self.glfw_window, x, y)

    def set_size(self, width, height):
        glfw.set_window_size(self.glfw_window, width, height)

    def event(self, func):
        num_params = len(inspect.signature(func).parameters)

        # Compare with .value to get the string values of Enum members
        if func.__name__ == Event.ON_DRAW.value and num_params != 0:
            raise ValueError(f"The '{Event.ON_DRAW.value}' event handler must accept exactly 0 parameters.")
        elif func.__name__ == Event.ON_MOUSE_PRESS.value and num_params != 1:
            raise ValueError(f"The '{Event.ON_MOUSE_PRESS.value}' event handler must accept exactly 1 parameter.")
        elif func.__name__ == Event.ON_MOUSE_RELEASE.value and num_params != 1:
            raise ValueError(f"The '{Event.ON_MOUSE_RELEASE.value}' event handler must accept exactly 1 parameter.")
        elif func.__name__ == Event.ON_MOUSE_MOVE.value and num_params != 2:
            raise ValueError(f"The '{Event.ON_MOUSE_MOVE.value}' event handler must accept exactly 2 parameters.")
        elif func.__name__ == Event.ON_WINDOW_CLOSE.value and num_params != 0:
            raise ValueError(f"The '{Event.ON_WINDOW_CLOSE.value}' event handler must accept exactly 0 parameters.")
        elif func.__name__ == Event.ON_WINDOW_RESIZE.value and num_params != 2:
            raise ValueError(f"The '{Event.ON_WINDOW_RESIZE.value}' event handler must accept exactly 2 parameters.")
        elif func.__name__ == Event.ON_WINDOW_FOCUS.value and num_params != 0:
            raise ValueError(f"The '{Event.ON_WINDOW_FOCUS.value}' event handler must accept exactly 0 parameters.")
        elif func.__name__ == Event.ON_WINDOW_UNFOCUS.value and num_params != 0:
            raise ValueError(f"The '{Event.ON_WINDOW_UNFOCUS.value}' event handler must accept exactly 0 parameters.")
        elif func.__name__ == Event.ON_KEY_PRESS.value and num_params != 2:
            raise ValueError(f"The '{Event.ON_KEY_PRESS.value}' event handler must accept exactly 2 parameters.")
        elif func.__name__ == Event.ON_KEY_RELEASE.value and num_params != 2:
            raise ValueError(f"The '{Event.ON_KEY_RELEASE.value}' event handler must accept exactly 2 parameters.")
        elif func.__name__ == Event.ON_WINDOW_ICONIFY.value and num_params != 0:
            raise ValueError(f"The '{Event.ON_WINDOW_ICONIFY.value}' event handler must accept exactly 0 parameters.")
        elif func.__name__ == Event.ON_WINDOW_MAXIMIZE.value and num_params != 0:
            raise ValueError(f"The '{Event.ON_WINDOW_MAXIMIZE.value}' event handler must accept exactly 0 parameters.")
        elif func.__name__ == Event.ON_WINDOW_RESTORE.value and num_params != 0:
            raise ValueError(f"The '{Event.ON_WINDOW_RESTORE.value}' event handler must accept exactly 0 parameters.")
        elif func.__name__ == Event.ON_KEY_REPEAT.value and num_params != 2:
            raise ValueError(f"The '{Event.ON_KEY_REPEAT.value}' event handler must accept exactly 2 parameters.")

        self.events[func.__name__] = func
        return func

    def mouse_button_callback(self, window, button, action, mods):
        if action == glfw.PRESS:
            self.call_event(Event.ON_MOUSE_PRESS.value, button)
        elif action == glfw.RELEASE:
            self.call_event(Event.ON_MOUSE_RELEASE.value, button)

    def cursor_position_callback(self, window, xpos, ypos):
        self.call_event(Event.ON_MOUSE_MOVE.value, xpos, ypos)

    def window_close_callback(self, window):
        self.call_event(Event.ON_WINDOW_CLOSE.value)

    def window_size_callback(self, window, width, height):
        self.call_event(Event.ON_WINDOW_RESIZE.value, width, height)

    def window_focus_callback(self, window, focused):
        if focused:
            self.call_event(Event.ON_WINDOW_FOCUS.value)
        else:
            self.call_event(Event.ON_WINDOW_UNFOCUS.value)

    def window_iconify_callback(self, window, iconify):
        self.call_event(Event.ON_WINDOW_ICONIFY.value)

    def window_maximize_callback(self, window, maximized):
        if maximized:
            self.call_event(Event.ON_WINDOW_MAXIMIZE.value)
        else:
            self.call_event(Event.ON_WINDOW_RESTORE.value)

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            self.call_event(Event.ON_KEY_PRESS.value, key, mods)
        elif action == glfw.RELEASE:
            self.call_event(Event.ON_KEY_RELEASE.value, key, mods)
        elif action == glfw.REPEAT:
            self.call_event(Event.ON_KEY_REPEAT.value, key, mods)

    def call_event(self, func_name, *args):
        if func_name in self.events:
            self.events[func_name](*args)

    def update(self):
        if glfw.get_window_attrib(self.glfw_window, glfw.VISIBLE):
            glfw.make_context_current(self.glfw_window)

            self.call_event(Event.ON_DRAW.value)

            glfw.swap_buffers(self.glfw_window)
            glfw.poll_events()

    @staticmethod
    def add_window(window):
        Window.windows.append(window)
