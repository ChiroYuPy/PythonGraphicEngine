from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT, glBegin, GL_QUADS, glVertex3fv, \
    glEnable, glMatrixMode, GL_DEPTH_TEST, GL_MODELVIEW, glEnd, GL_DEPTH_BUFFER_BIT, glTranslatef
from OpenGL.raw.GL.VERSION.GL_1_0 import glPushMatrix, glPopMatrix

from camera import Camera
from components import Mesh, Transform


class RenderSystem:
    def __init__(self, window):
        self.window = window

        glEnable(GL_DEPTH_TEST)
        Camera.main.apply_perspective()  # Apply camera perspective settings
        glMatrixMode(GL_MODELVIEW)

    def render(self, entities):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers

        Camera.main.apply_view()  # Apply the camera view transformation

        for entity in entities:
            # Get Mesh and Transform components from the entity
            mesh = entity.get_component(Mesh)
            transform = entity.get_component(Transform)

            # Apply the entity's transformation
            glPushMatrix()  # Save the current matrix
            glTranslatef(transform.position.x, transform.position.y, transform.position.z)  # Translate entity

            # Draw the object as quads (faces)
            faces = [
                (0, 1, 2, 3),  # Back face
                (4, 5, 6, 7),  # Front face
                (0, 1, 5, 4),  # Bottom face
                (2, 3, 7, 6),  # Top face
                (0, 3, 7, 4),  # Left face
                (1, 2, 6, 5)   # Right face
            ]

            glBegin(GL_QUADS)
            for face in faces:
                for vertex in face:
                    glVertex3fv(mesh.vertices[vertex])
            glEnd()

            glPopMatrix()  # Restore the previous matrix
