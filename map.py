import pygame
from pygame.locals import *
from maze.maze import Maze
import render

def show_map(display_surf):
    drawList = [[200,150], [600,150], [200,450], [600,450]]
    white = ((255, 255, 255))
    for a,b in drawList:
        #Central rectangle
        pygame.draw.rect(display_surf, white, (a-70, b-40, 140, 80))

        #side line
        pygame.draw.line(display_surf, white, [a+70, b+40], [a+140, b+100], 2)
        pygame.draw.line(display_surf, white, [a+70, b-40], [a+140, b-100], 2)
        pygame.draw.line(display_surf, white, [a-70, b+40], [a-140, b+100], 2)
        pygame.draw.line(display_surf, white, [a-70, b-40], [a-140, b-100], 2)
        
    