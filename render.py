import pygame
from pygame.locals import *
from map import show_map

def front_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    title = font.render("4D Maze", True, (255, 255, 255))
    display_surf.blit(title, (400, 300))
    pygame.display.flip()

def play_render(font, maze, display_surf):
    display_surf.fill((255, 255, 255))
    for i in range(4):
        show_map(i)
    pygame.display.flip()
#