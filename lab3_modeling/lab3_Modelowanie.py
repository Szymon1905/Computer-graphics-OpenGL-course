#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy
import random as r


n = 11  # liczba dokładności, nieparzyste wygląda lepiej
u = numpy.linspace(0, 1, n)  # punkty od 0 do 1,  n - liczba punktów jakie mamy otrzymać, wliczając 0 i 1
v = numpy.linspace(0, 1, n)
tab = numpy.zeros((n, n, 3))  # tablica n x n x 3, 3 ponieważ dla kazdego obliczamy: x y z


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():  # rysowanie osi
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)  # oś czerwona
    glVertex3f(-6.0, 0.0, 0.0)
    glVertex3f(6.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)  # oś zielona
    glVertex3f(0.0, -6.0, 0.0)
    glVertex3f(0.0, 6.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)  # oś niebieska
    glVertex3f(0.0, 0.0, -6.0)
    glVertex3f(0.0, 0.0, 6.0)

    glEnd()


def punkty(tab, n):
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 1.0)  # jasno niebieskie
    for i in range(n):
        for j in range(n):
            glVertex3fv(tab[i][j])  # automatycznie zwraca 3 elemty z ostatniej tablicy
    glEnd()

def linie_proste(tab, n):
    glBegin(GL_LINES)
    for i in range(n-1):
        for j in range(n-1):
            glColor3f(1.0, 0.5, 0.0)       # pomarańczowe
            glVertex3fv(tab[i][j])  # i - pionowe
            glVertex3fv(tab[i + 1][j])

            glColor3f(0.0, 1.0, 1.0)  # jasno niebieskie
            glVertex3fv(tab[i][j])  # j - poziome
            glVertex3fv(tab[i][j + 1])
    glEnd()

def linie_po_skosie(tab, n):
    glBegin(GL_LINES)
    for i in range(n):
        for j in range(n):   # for j in range(n-1):
            if (i < n and j != n-1 and i != n-1): # i + 1 ponieważ jaknie było to sie rysowął wszytsko
                glColor3f(0.0, 1.0, 0.0)  # jasno niebieskie
                glVertex3fv(tab[i][j])  # i - pionowe
                glColor3f(1.0, 0.0, 0.0)
                glVertex3fv(tab[i + 1][j + 1])  # glVertex3fv(tab[i + 1][j + 1])
            else:
                glVertex3fv(tab[n-1][0])  # i - pionowe
                glVertex3fv(tab[0][n-1])

            if (j < n and j != n-1):
                glColor3f(0.0, 1.0, 1.0)
                glVertex3fv(tab[i][j])  # j - poziome
                glVertex3fv(tab[i][j + 1])
    glEnd()


def trojkaty(tab, n):
    r.seed(2)
    glBegin(GL_TRIANGLES)
    for i in range(n-1):
        for j in range(n-1): # index error jak sie przesuwa na j + 1
            color = (r.random(), r.random(), r.random())
            glColor3f(color[0], color[1], color[2])
            glVertex3fv(tab[i][j])

            color = (r.random(), r.random(), r.random())
            glColor3f(color[0], color[1], color[2])
            glVertex3fv(tab[i + 1][j])

            color = (r.random(), r.random(), r.random())
            glColor3f(color[0], color[1], color[2])
            glVertex3fv(tab[i][j + 1])

            color = (r.random(),r.random(),r.random())
            glColor3f(color[0], color[1], color[2])
            glVertex3fv(tab[i + 1][j])

            color = (r.random(), r.random(), r.random())
            glColor3f(color[0], color[1], color[2])
            glVertex3fv(tab[i + 1][j + 1])

            color = (r.random(), r.random(), r.random())
            glColor3f(color[0], color[1], color[2])
            glVertex3fv(tab[i][j + 1])
    glEnd()

# przepisany wzór na jajko
for i in range(n):
    for j in range(n):
        tab[i][j][0] = (-90 * (u[i]**5) + 225 * (u[i]**4) - 270 * (u[i]**3) + 180 * (u[i]**2) - 45 * u[i]) * math.cos(math.pi * v[j])
        tab[i][j][1] = (160 * (u[i]**4) - 320 * (u[i]**3) + 160 * (u[i]**2)) - 5  # minus 5 aby sie wyswietlało na srodku
        tab[i][j][2] = (-90 * (u[i]**5) + 225 * (u[i]**4) - 270 * (u[i]**3) + 180 * (u[i]**2) - 45 * u[i]) * math.sin(math.pi * v[j])


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    kat_obrotu = (time * 90 / math.pi)  # zmiana liczby zmeinia predokos obratu w czasie

    # glrotatef - # kat obrotu, kolejne 3 wektor wokór którego się obraca
    glRotatef(kat_obrotu, 1, 1, 0)

    #punkty(tab, n)
    linie_proste(tab, n)
    #trojkaty(tab, n)
    #linie_po_skosie(tab, n)
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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


main()
