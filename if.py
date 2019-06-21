import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *


vertices = (
    #-- Caixas feitas de baixo para Cima

    # -- Letra I --
    # Caixa 1
    (-1, 0, 0),
    (-1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),

    # Caixa 2
    (0.1, 0, 0),
    (1.1, 0, 0),
    (0.1, 1, 0),
    (1.1, 1, 0),

    # Caixa 3
    (-1, 1.1, 0),
    (0, 1.1, 0),
    (-1, 2.1, 0),
    (0, 2.1, 0),

    # -- Letra F
    # Caixa 4
    (0.1, 1.1, 0),
    (1.1, 1.1, 0),
    (0.1, 2.1, 0),
    (1.1, 2.1, 0),

    # Caixa 5
    (-1, -0.1, 0),
    (0, -0.1, 0),
    (0, -1.1, 0),
    (-1, -1.1, 0),

    # Caixa 6
    (0.1, -0.1, 0),
    (1.1, -0.1, 0),
    (0.1, -1.1, 0),
    (1.1, -1.1, 0),

    # Caixa 7
    (0.1, 2.2, 0),
    (1.1, 2.2, 0),
    (0.1, 3.2, 0),
    (1.1, 3.2, 0),

    # Caixa 8
    (1.2, 3.2, 0),
    (1.2, 2.2, 0),
    (2.2, 2.2, 0),
    (2.2, 3.2, 0),

    # Caixa 9
    (1.2, 0, 0),
    (1.2, 1, 0),
    (2.2, 1, 0),
    (2.2, 0, 0),


)


edges = (

    # -- Letra I --
    # Caixa 1
    (0, 1),
    (0, 3),
    (1, 2),
    (2, 3),

    # Caixa 2
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7),

    # Caixa 3
    (8, 9),
    (8, 10),
    (9, 11),
    (10, 11),

    # -- Letra F --
    # Caixa 4
    (12, 13),
    (12, 14),
    (13, 15),
    (14, 15),

    # Caixa 5
    (16, 17),
    (16, 19),
    (17, 18),
    (18, 19),

    # Caixa 6
    (20, 21),
    (20, 22),
    (21, 23),
    (22, 23),

    # Caixa 7
    (24, 25),
    (24, 26),
    (25, 27),
    (26, 27),

    # Caixa 8
    (28, 29),
    (28, 31),
    (29, 30),
    (30, 31),

    # Caixa 9
    (32, 33),
    (32, 35),
    (33, 34),
    (34, 35),

)


def If():
    glLineWidth(4)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def Circle(x, y, side, radius):
    posx, posy = x, y
    sides = side
    radius = radius
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i*2*pi/sides) + posx
        sine = radius * sin(i*2*pi/sides) + posy
        glVertex2f(cosine, sine)
    glEnd()


def main():
    pygame.init()
    display = (600, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0, 0, -10)

    clock = pygame.time.Clock()
    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(1, 0, 0)
        Circle(-0.5, 2.75, 30, 0.5)

        glColor3f(0, 1, 0)
        If()

        pygame.display.flip()


main()