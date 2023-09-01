import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Initialize GLUT
glutInit()

# Player position
player_x, player_y, player_z = 0, 0, 0

# Blocks
blocks = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            player_z += 0.1
        if keys[K_s]:
            player_z -= 0.1
        if keys[K_a]:
            player_x += 0.1
        if keys[K_d]:
            player_x -= 0.1

        # Place block on left mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            block_x = round(player_x) + round(mouse_x / display[0]) * 2 - 1
            block_y = round(player_y) - round(mouse_y / display[1]) * 2 + 1
            blocks.append((block_x, block_y))

        # Destroy block on right mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            block_x = round(player_x) + round(mouse_x / display[0]) * 2 - 1
            block_y = round(player_y) - round(mouse_y / display[1]) * 2 + 1
            if (block_x, block_y) in blocks:
                blocks.remove((block_x, block_y))

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw cube
    for block in blocks:
        glBegin(GL_QUADS)
        glVertex3f(block[0] - 0.5, -1, block[1] + 0.5)
        glVertex3f(block[0] - 0.5, 1, block[1] + 0.5)
        glVertex3f(block[0] + 0.5, 1, block[1] + 0.5)
        glVertex3f(block[0] + 0.5, -1, block[1] + 0.5)
        glEnd()

    # Draw player
    glPushMatrix()
    glTranslatef(player_x, 0, player_y)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

# Clean up
pygame.quit()
