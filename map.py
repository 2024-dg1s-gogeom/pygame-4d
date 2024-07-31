import pygame
from pygame.locals import *
from maze.maze import Maze
import render

def show_map(display_surf):
    drawList = [[200,150], [600,150], [200,450], [600,450]]
    white = ((255, 255, 255))
    black = ((0, 0, 0))
    for a,b in drawList:
        pygame.draw.line(display_surf, white, [a+85, b+65], [a+155, b+115], 2)
        pygame.draw.line(display_surf, white, [a+85, b-65], [a+155, b-115], 2)
        pygame.draw.line(display_surf, white, [a-85, b+65], [a-155, b+115], 2)
        pygame.draw.line(display_surf, white, [a-85, b-65], [a-155, b-115], 2)

        pygame.draw.line(display_surf, white, [a-85, b-65], [a+85, b-65], 2)
        pygame.draw.line(display_surf, white, [a-85, b+65], [a+85, b+65], 2)
        pygame.draw.line(display_surf, white, [a-155, b-115], [a+155, b-115], 2)
        pygame.draw.line(display_surf, white, [a-155, b+115], [a+155, b+115], 2)
        pygame.draw.line(display_surf, white, [a-85, b-65], [a-85, b+65], 2)
        pygame.draw.line(display_surf, white, [a+85, b-65], [a+85, b+65], 2)
        pygame.draw.line(display_surf, white, [a-155, b-115], [a-155, b+115], 2)
        pygame.draw.line(display_surf, white, [a+155, b-115], [a+155, b+115], 2)

    pygame.draw.line(display_surf, white, [355,265], [445,265], 2)
    pygame.draw.line(display_surf, white, [355,335], [445,335], 2)
    pygame.draw.line(display_surf, white, [355,265], [355,335], 2)
    pygame.draw.line(display_surf, white, [445,265], [445,335], 2)

    pygame.draw.line(display_surf, black, [400,265], [400,335], 3)
    pygame.draw.line(display_surf, black, [355,300], [445,300], 3)
        
    