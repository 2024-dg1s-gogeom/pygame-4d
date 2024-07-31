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

        #Frame
        pygame.draw.rect(display_surf, white, (a-162, b-102, 324, 204))
        
        #cross line
        pygame.draw.line(display_surf, white, (400,0), (400,600), 2)
        pygame.draw.line(display_surf, white, (0,300), (800,300), 2)

        #side polygon
        pygame.draw.polygon(display_surf, black, [[a+120, b+60], [a+160, b+100], [a-160, b+100], [a-120, b+60]])
        pygame.draw.polygon(display_surf, black, [[a+120, b-60], [a+160, b-100], [a-160, b-100], [a-120, b-60]])
        pygame.draw.polygon(display_surf, black, [[a+120, b+60], [a+160, b+100], [a+160, b-100], [a+120, b-60]])
        pygame.draw.polygon(display_surf, black, [[a-120, b+60], [a-160, b+100], [a-160, b-100], [a-120, b-60]])
        
        #side line
        pygame.draw.line(display_surf, white, [a+120, b+60], [a+160, b+100], 2)
        pygame.draw.line(display_surf, white, [a+120, b-60], [a+160, b-100], 2)
        pygame.draw.line(display_surf, white, [a-120, b+60], [a-160, b+100], 2)
        pygame.draw.line(display_surf, white, [a-120, b-60], [a-160, b-100], 2)

        #Central Frame
        pygame.draw.rect(display_surf, white, (a-120, b-60, 240, 120))

        #Cetral rectangle
        pygame.draw.rect(display_surf, black, (a-118, b-58, 236, 116))

        #Coordinate
    text_List=[["XP", (200,150)], ["YP", (600, 150)], ["ZP", (200, 450)], ["WP", (600, 450)]]
    for C, X in text_List:
        font=pygame.font.Font(None, 40)
        text=font.render(C, True, white)
        display_surf.blit(text, X)
    pygame.display.flip()

        
    