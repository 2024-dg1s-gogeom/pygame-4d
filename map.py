import pygame
from pygame.locals import *
from maze.maze import Maze
import render

def show_map(display_surf):
    drawList = [[200,150], [600,150], [200,450], [600,450]]
    gray = (200, 200, 200)
    black= (0, 0, 0)
    white= (255, 255, 255)
    for a,b in drawList:
        #Background cell
        pygame.draw.rect(display_surf, black, (a-200, b-150, 400, 300))

        #cross line
        pygame.draw.line(display_surf, white, (400,0), (400,600), 2)
        pygame.draw.line(display_surf, white, (0,300), (800,300), 2)  

        #Frame
        pygame.draw.rect(display_surf, white, (a-162, b-102, 324, 204))
        
        #Central Frame
        pygame.draw.rect(display_surf, white, (a-120, b-60, 240, 120))

        #Cetral rectangle
        pygame.draw.rect(display_surf, black, (a-118, b-68, 236, 136))

        #side polygon
        ps1=[a+120, b+60], [a+160, b+100], [a-160, b+100], [a-120, b+60]
        ps2=[a+120, b-60], [a+160, b-100], [a-160, b-100], [a-120, b-60]
        ps3=[a+120, b+60], [a+160, b+100], [a+160, b-100], [a+120, b-60]
        ps4=[a-120, b+60], [a-160, b+100], [a-160, b-100], [a-120, b-60]
        pygame.draw.polygon(display_surf, gray, ps1)
        pygame.draw.polygon(display_surf, gray, ps2)
        pygame.draw.polygon(display_surf, gray, ps3)
        pygame.draw.polygon(display_surf, gray, ps4)
        
        #side line
        pygame.draw.line(display_surf, white, [a+120, b+60], [a+160, b+100], 2)
        pygame.draw.line(display_surf, white, [a+120, b-60], [a+160, b-100], 2)
        pygame.draw.line(display_surf, white, [a-120, b+60], [a-160, b+100], 2)
        pygame.draw.line(display_surf, white, [a-120, b-60], [a-160, b-100], 2)