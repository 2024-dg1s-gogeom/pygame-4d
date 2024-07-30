import pygame
from pygame.locals import *
from map import show_map

def front_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    title = font.render("Tap SPACE BAR to Start", True, (255, 255, 255))
    display_surf.blit(title, (210, 272))
    pygame.display.flip()

def play_render(font, maze, display_surf):
    display_surf.fill((255, 255, 255))
    half_width = 400
    half_height = 300
    display_surf.fill((0, 0, 0), rect=(0, 0, half_width, half_height))
    display_surf.fill((0, 0, 0), rect=(400, 300, half_width, half_height))  
    for i in range(4):
        show_map(i)
    pygame.display.flip()

def finish_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    ending = font.render("You WON !!", True, (255, 255, 255))
    display_surf.blit(ending, (370, 232))
    goingback = font.render("Tap ESC to return to start")
    display_surf.blit(goingback, (345, 282))


