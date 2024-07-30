import pygame
from pygame.locals import *
from maze.maze import Maze
import render

def show_map(display_surf):
    drawList = [[200,150], [600,150], [200,450], [600,450]]
    white = ((255, 255, 255))
    for a,b in drawList:

        #side line
        pygame.draw.line(display_surf, white, [a+85, b+65], [a+155, b+115], 2)
        pygame.draw.line(display_surf, white, [a+85, b-65], [a+155, b-115], 2)
        pygame.draw.line(display_surf, white, [a-75, b+55], [a-155, b+115], 2)
        pygame.draw.line(display_surf, white, [a-75, b-65], [a-155, b-115], 2)
        
    