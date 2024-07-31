import pygame
from pygame.locals import *
from maze.maze import Maze
import render

def show_map(display_surf):
    drawList = [[200,150], [600,150], [200,450], [600,450]]
    gray = ((200, 0, 0))
    black= ((0, 0, 0))
    for a,b in drawList:
        #Frame rectangle
        pygame.draw.rect(display_surf, gray, (a-160, b-100, 320, 200))
        
        #Central rectangle
        pygame.draw.rect(display_surf, black, (a-120, b-60, 240, 120))

        #side polygon
        pygame.draw.polygon(display_surf, gray, [a+120, b+60], [a+160, b+100], [a-120, b+60], [a-160, b+100])
        pygame.draw.polygon(display_surf, gray, [a+120, b-60], [a+160, b-100], [a-120, b-60], [a-160, b-100])
        pygame.draw.polygon(display_surf, gray, [a+120, b+60], [a+160, b+100], [a+120, b-60], [a+160, b-100])
        pygame.draw.polygon(display_surf, gray, [a-120, b+60], [a-160, b+100], [a-120, b-60], [a-160, b-100])
        
        #side line
        pygame.draw.line(display_surf, black, [a+120, b+60], [a+160, b+100], 2)
        pygame.draw.line(display_surf, black, [a+120, b-60], [a+160, b-100], 2)
        pygame.draw.line(display_surf, black, [a-120, b+60], [a-160, b+100], 2)
        pygame.draw.line(display_surf, black, [a-120, b-60], [a-160, b-100], 2)
        
    