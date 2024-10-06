from OpenGL.raw.GL.VERSION.GL_1_0 import glMatrixMode, GL_PROJECTION, glLoadIdentity, glTranslatef, GL_MODELVIEW, \
    glRotatef
from OpenGL.raw.GLU import gluPerspective

from vector import Vector3


class Camera:
    def __init__(self, position=Vector3(0.0, 0.0, -10.0), rotation=Vector3(0.0, 0.0, 0.0), fov=90.0, aspect_ratio=800 / 600, near=0.1, far=50.0):
        self.position = position
        self.rotation = rotation

        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near = near
        self.far = far

        self.set_main_camera(self)

    def set_position(self, position):
        self.position = position

    def apply_perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov, self.aspect_ratio, self.near, self.far)
        glMatrixMode(GL_MODELVIEW)

    def apply_view(self):
        glLoadIdentity()
        glRotatef(-self.rotation.x, 1.0, 0.0, 0.0)  # Rotate around x-axis
        glRotatef(-self.rotation.y, 0.0, 1.0, 0.0)  # Rotate around y-axis
        glTranslatef(self.position.x, self.position.y, self.position.z)  # Move camera to position

    @staticmethod
    def set_main_camera(camera):
        Camera.main = camera