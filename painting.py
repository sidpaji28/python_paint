import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
DRAW_COLOR = (0, 0, 0)
FILL_COLOR = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing with Fill")

# Variables
drawing = False
points = []

def draw():
    for point in points:
        pygame.draw.circle(screen, DRAW_COLOR, point, 2)

def fill_color(x, y):
    pygame.draw.floodfill(screen, (x, y), FILL_COLOR)

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                points.append(event.pos)
            elif event.button == 3:
                fill_color(event.pos[0], event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                points.append(event.pos)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

