
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(x, y, a, b):
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 90.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-90.0, 50.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(90.0, 50.0)

    glEnd()

    hex = 0xcc3592                # kolory tak łatwiej wybrać
    czerwony = (hex >> 16) & 0xFF
    zielony = (hex >> 8) & 0xFF
    niebieski = hex & 0xFF

    glColor3ub(czerwony, zielony, niebieski)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - (0.5 * a), y + (0.5 * b))
    glVertex2f((x + (0.5 * a)), y + (0.5 * b))
    glVertex2f((x + (0.5 * a)), y - (0.5 * b))
    glEnd()

    hex = 0x006666
    czerwony = (hex >> 16) & 0xFF
    zielony = (hex >> 8) & 0xFF
    niebieski = hex & 0xFF

    glColor3ub(czerwony, zielony, niebieski)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + (0.5 * a), y - (0.5 * b))
    glVertex2f((x - (0.5 * a)), y - (0.5 * b))
    glVertex2f((x - (0.5 * a)), y + (0.5 * b))
    glEnd()

    glColor3f(0.0, 0.0, 0.0)  # czarny punkt żeby było widać gdzie środek
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glEnd()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, "Szymon Borzdyński", None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(0, 0, 100, 70)

        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
