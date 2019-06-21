import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

vertices = (
    # --Frente--

    # Portão
    (0.5, 0, 0), #0
    (0.5, 1.5, 0),#1
    (2, 1.5, 0),#2
    (2, 0, 0),#3

    # CaixaCentral
    (-1, 0, 0),#4
    (-1, 2, 0),#5
    (3.5, 2, 0),#6
    (3.5, 0, 0),#7

    # Torre da Esquerda
    (-2, 0, 0),#8
    (-2, 3, 0),#9
    (-1, 3, 0),#10

    # Torre da Direita
    (4.5, 0, 0),#11
    (4.5, 3, 0),#12
    (3.5, 3, 0),#13

    # Caixas Torre da Esquerda
    (-2, 3.2, 0),#14
    (-1.7, 3.2, 0),#15
    (-1.7, 3, 0),#16

    (-1, 3.2, 0),#17
    (-1.3, 3.2, 0),#18
    (-1.3, 3, 0),#19

    # Caixas Torre da Direita
    (4.5, 3.2, 0),#20
    (4.2, 3.2, 0),#21
    (4.2, 3, 0),#22

    (3.5, 3.2, 0),#23
    (3.8, 3.2, 0),#24
    (3.8, 3, 0),#25
    #-----------------------------------------
    #-----------------------------------------

    # --Atrás--

    # Caixa Central
    (-1, 0, -1),#26
    (-1, 2, -1),#27
    (3.5, 2, -1),#28
    (3.5, 0, -1),#29

    # Torre da Esquerda
    (-2, 0, -1),#30
    (-2, 3, -1),#31
    (-1, 3, -1),#32

    # Torre da Direita
    (4.5, 0, -1),#33
    (4.5, 3, -1),#34
    (3.5, 3, -1),#35

    # Caixas da Torre da Esquerda
    (-2, 3.2, -1),#36
    (-1.7, 3.2, -1),#37
    (-1.7, 3, -1),#38

    (-1, 3.2, -1),#39
    (-1.3, 3.2, -1),#40
    (-1.3, 3, -1),#41

    # Caixas da Torre da Direita
    (4.5, 3.2, -1),#42
    (4.2, 3.2, -1),#43
    (4.2, 3, -1),#44

    (3.5, 3.2, -1),#45
    (3.8, 3.2, -1),#46
    (3.8, 3, -1),#47
)
    #-----------------------------------------
    #-----------------------------------------

edges = (

    # --Frente--

    # Porta
    (0, 1),
    (0, 3),
    (1, 2),
    (2, 3),

    # Caixa Central
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),


    # Torre da Esquerda
    (4, 8),
    (8, 9),
    (9, 10),
    (10, 4),

    # Torre da Direita
    (7, 11),
    (11, 12),
    (12, 13),
    (13, 7),

    # Caixas Torre da Esquerda
    (9, 14),
    (14, 15),
    (15, 16),

    (10, 17),
    (17, 18),
    (18, 19),

    # Caixas Torre da Direita
    (12, 20),
    (20, 21),
    (21, 22),

    (13, 23),
    (23, 24),
    (24, 25),

    #-----------------------------------------
    #-----------------------------------------

    # --Atrás--

    # Portao
    (26, 27),
    (27, 28),
    (28, 29),
    (29, 26),

    # Torre da Esquerda
    (26, 30),
    (30, 31),
    (31, 32),
    (32, 26),

    # Torre da Direita
    (29, 33),
    (33, 34),
    (34, 35),
    (35, 29),

    # Caixas da Torre Esquerda
    (31, 36),
    (36, 37),
    (37, 38),

    (32, 39),
    (39, 40),
    (40, 41),

    # Caixas da Torre Direita
    (34, 42),
    (42, 43),
    (43, 44),

    (35, 45),
    (45, 46),
    (46, 47),

    #-----------------------------------------
    #-----------------------------------------

    # Conexão Entre Frente e Atrás
    (4, 26),
    (7, 29),
    (9, 31),
    (10, 32),
    (12, 34),
    (13, 35),
    (30, 8),
    (14, 36),
    (15, 37),
    (16, 38),
    (17, 39),
    (18, 40),
    (19, 41),
    (5, 27),
    (6, 28),
    (42, 20),
    (43, 21),
    (44, 22),
    (45, 23),
    (46, 24),
    (47, 25),
    (33, 11),
)

planos = (
    # Portao
    (4, 5, 6, 7),
    (26, 27, 28, 29),
    (5, 6, 28, 27),
    (8, 11, 33, 30),

    # Torre da Esquerda
    (4, 8, 9, 10),
    (9, 14, 15, 16),
    (10, 17, 18, 19),
    (14, 15, 37, 36),
    (17, 18, 40, 39),
    (8, 14, 36, 30),
    (26, 30, 31, 32),
    (31, 36, 37, 38),
    (32, 39, 40, 41),
    (4, 17, 39, 26),
    (15, 16, 38, 37),
    (18, 19, 41, 40),
    (16, 19, 41, 38),

    # Torre da Direita
    (7, 11, 12, 13),
    (29, 33, 34, 35),
    (33, 11, 20, 42),
    (7, 23, 45, 29),
    (12, 20, 21, 22),
    (13, 23, 24, 25),
    (34, 42, 43, 44),
    (35, 45, 46, 47),
    (20, 21, 43, 42),
    (23, 24, 46, 45),
    (22, 25, 47, 44),

)
colors = (
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),
	(1,1,1),

)

def CriarCastelo():
    glBegin(GL_QUADS)
    for plano in planos:
        x = 0
        for vertex in plano:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glLineWidth(0.5)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
            glColor3f(0, 0, 0)
    glEnd()


def Circle(x, y, side, radius):
    glColor3fv((0, 0, 0))
    posx, posy = x, y
    glBegin(GL_POLYGON)
    for i in range(side):
        cosine = radius * cos(i * 2 * pi / side) + posx
        sine = radius * sin(i * 2 * pi / side) + posy
        glVertex2f(cosine, sine)
    glEnd()


def main():
    pygame.init()
    display = (850, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(50, (display[0] / display[1]), 0.1, 50)

    glTranslatef(0, -1, -10)

    clock = pygame.time.Clock()

    while True:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0.5)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        CriarCastelo()
        Circle(-1.5, 2.5, 20, 0.3)
        Circle(4, 2.5, 20, 0.3)
        pygame.display.flip()


main()
