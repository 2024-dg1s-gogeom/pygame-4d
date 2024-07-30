import pygame
from pygame.locals import *
from maze.maze import Maze
import render

def show_map(display_surf):
    drawList = [[200,150], [600,150], [200,450], [600,450]]
    white = ((255, 255, 255))
    for a,b in drawList:
        #Central Rectangle
        pygame.draw.rect(display_surf, white, (a-80, b-60, 160, 120))
        #side line
        pygame.draw.line(display_surf, white, [a+80, b+60], [a+160, b+120], 2)
        pygame.draw.line(display_surf, white, [a+80, b-60], [a+160, b-120], 2)
        pygame.draw.line(display_surf, white, [a-80, b+60], [a-160, b+120], 2)
        pygame.draw.line(display_surf, white, [a-80, b-60], [a-160, b-120], 2)
        
        #Outside Frame
        pygame.draw.rect(display_surf, white, (a-160, b-120, 320, 240))
    