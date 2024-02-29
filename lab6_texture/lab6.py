import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

from PIL import Image

schowaj = True

image = Image.open(r"Wlasna_tekstura.tga")
image2 = Image.open(r"tfasz2.tga")

zmiana = False
viewer = [0.0, 0.0, 10.0]

theta = 0.0
phi = 0.0
pix2angle = 1.0
q = 1

left_mouse_button_pressed = 0
mouse_y_pos_old = 0
mouse_x_pos_old = 0
delta_x = 0
delta_y = 0

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001


def startup():
    global image, image2
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_CULL_FACE)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # image = Image.open(r"C:\Users\Dom\PycharmProjects\grafika_ALL\D1_t.tga")


def shutdown():
    pass


def orginalne():
    glBegin(GL_TRIANGLES)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, -5.0, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(5.0, -5.0, 0.0)
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0.0, 5.0, 0.0)
    glEnd()


def kwadrat():
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-4.0, -4.0, 0.0)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(4.0, -4.0, 0.0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(4.0, 4.0, 0.0)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-4.0, 4.0, 0.0)
    glEnd()


def serce():
    glBegin(GL_POLYGON)

    # glTexCoord2f(0.0, 0.0)
    # glVertex3f(0.0, 0.0, 0.0)

    # glTexCoord2f(0.5, 0.75)
    glVertex3f(3.22, 1.76, 0.0)

    # glTexCoord2f(0.25, 0.1)

    # glTexCoord2f(0.25, 0.9)
    glVertex3f(3.87, 1.26, 0.0)

    glVertex3f(4.38, 1.8, 0.0)

    glVertex3f(3.21, 3.24, 0.0)

    # glTexCoord2f(0.0, 0.75)
    glVertex3f(2.07, 1.79, 0.0)

    # glTexCoord2f(1.0, 0.75)

    # glTexCoord2f(0.5, 0.0)

    glVertex3f(2.5, 1.26, 0.0)

    glEnd()

    #     ____________________
    #     | 4              3 |
    #     |                  |
    #     |                  |
    #     |                  |
    #     |                  |
    #     | 1              2 |
    #     |__________________|


def ostrosłup(schowaj):
    glBegin(GL_TRIANGLE_FAN)

    glTexCoord2f(0.5, 0.5)  # czubek
    glVertex3f(0.0, 0.0, 4.0)

    glTexCoord2f(0.0, 0.0)  # wierzchołek 1
    glVertex3f(-5.0, -5.0, 0.0)

    if schowaj:
        glTexCoord2f(1.0, 0.0)  # wierzchołek 2       1------------2------------3
        glVertex3f(5.0, -5.0, 0.0)

    glTexCoord2f(1.0, 1.0)  # wierzchołek 3  1,1  nie widać
    glVertex3f(5.0, 5.0, 0.0)

    glTexCoord2f(0.0, 1.0)  # wierzchołek 4            4------------1
    glVertex3f(-5.0, 5.0, 0.0)

    glTexCoord2f(0.0, 0.0)    # wierzchołek 1
    glVertex3f(-5.0, -5.0, 0.0)

    glEnd()


def ostrosłup_na_odwrot(schowaj):
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(0.0, 5.0, 0.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, 0.0, -5.0)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-5.0, 0.0, 5.0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(5.0, 0.0, 5.0)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(5.0, 0.0, -5.0)

    if schowaj:
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-5.0, 0.0, -5.0)

    glEnd()


def bochomaz(schowaj):
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(0.0, 5.0, 0.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, 0.0, -5.0)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-5.0, 0.0, 5.0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(5.0, 0.0, 5.0)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(5.0, 0.0, -5.0)

    if schowaj:
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-5.0, 0.0, -5.0)

    glEnd()


def render(time):
    global theta, phi, image, image2, zmiana
    if zmiana:
        glTexImage2D(
            GL_TEXTURE_2D, 0, 3, 256, 256, 0,
            GL_RGB, GL_UNSIGNED_BYTE, image.tobytes("raw", "RGB", 0, -1)
        )
    else:
        glTexImage2D(
            GL_TEXTURE_2D, 0, 3,  image2.size[0], image2.size[1], 0,
            GL_RGB, GL_UNSIGNED_BYTE, image2.tobytes("raw", "RGB", 0, -1)
        )

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle
    glRotatef(theta, 0.0, 1.0, 0.0)
    if left_mouse_button_pressed:
        phi += delta_y * pix2angle
    glRotatef(phi, 1.0, 0.0, 0.0)

    # kwadrat()     # todo figury

    ostrosłup(schowaj)

    # ostrosłup_na_odwrot(schowaj)

    # serce() # nie ukończone

    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global q, zmiana, schowaj
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    if key == GLFW_KEY_P and action == GLFW_PRESS:
        schowaj = not schowaj
        print("schowaj = ",schowaj)

    if key == GLFW_KEY_L and action == GLFW_RELEASE:
        zmiana = not zmiana
        print("zmiana")


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old
    global delta_y
    global mouse_y_pos_old

    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    print("Nacisnąć P aby uciąć kawałek")
    print("Nacisnąć L aby zmienić teksture")
    main()
