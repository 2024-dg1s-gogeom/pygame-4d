import pygame
from pygame.locals import *

def front_render(font, display_surf):
    display_surf.fill((0, 0, 0))
    title = font.render("4D Maze", True, (255, 255, 255))
    display_surf.blit(title, (400, 300))
    pygame.display.flip()

def play_render(font, display_surf):
    display_surf.fill((255, 255, 255))
    pygame.display.flip()