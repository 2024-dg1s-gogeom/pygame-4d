import pygame
from pygame.locals import *
from maze.maze import Maze
from maze.maze import mazePath
import numpy as np
def show_map(display_surf):
    from main import App
    drawList = [[200, 150, App.playerpos[0]+1, App.playerpos[1], App.playerpos[2], App.playerpos[3], App.playerpos[0]-1, App.playerpos[1], App.playerpos[2], App.playerpos[3], 1], [600, 150, App.playerpos[0], App.playerpos[1]+1, App.playerpos[2], App.playerpos[3], App.playerpos[0], App.playerpos[1]-1, App.playerpos[2], App.playerpos[3], 2]
                ,[200, 450, App.playerpos[0], App.playerpos[1], App.playerpos[2]+1, App.playerpos[3], App.playerpos[0], App.playerpos[1], App.playerpos[2]-1, App.playerpos[3], 3], [600, 450, App.playerpos[0], App.playerpos[1], App.playerpos[2], App.playerpos[3]+1, App.playerpos[1], App.playerpos[2], App.playerpos[3]-1, 4]]
    backup=drawList
    global gray, black, white
    gray = (180, 180, 180)
    black= (0, 0, 0)
    white= (255, 255, 255)
    for a, b, i1, i2, i3, i4, i5, i6, i7, i8, vi in drawList:
        c,d=drawList[vi-1][0], drawList[vi-1][1]
        #비교기
        if mazePath[i5][i6][i7][i8]==1:
            pygame.draw.rect(display_surf, black, (c-200, d-150, 400, 300))
            pygame.draw.rect(display_surf, white, (c-162, d-102, 324, 204))
            pygame.draw.rect(display_surf, white, (c-110, d-60, 220, 120))   
        else: 
            pygame.draw.rect(display_surf, gray, (c-200, d-150, 400, 300))
            pygame.draw.rect(display_surf, white, (c-162, d-102, 324, 204))
            pygame.draw.rect(display_surf, white, (c-110, d-60, 220, 120))
            
        if mazePath[i1][i2][i3][i4]==1:
            pygame.draw.rect(display_surf, black, (c-106, d-58, 212, 116))
        else:
            pygame.draw.rect(display_surf, gray, (c-106, d-58, 212, 116))
        for i in range(0,vi):
            di=drawList[i]
        for i in range(0,vi):
            di.remove(drawList[0])
        drawList.append(di)
        if mazePath[drawList[0][6]][drawList[0][7]][drawList[0][8]][drawList[0][9]]==1:
            pygame.draw.polygon(display_surf, black, [[c+110, d-60], [c+160, d-100], [c+160, d+100], [c+110, d+60]])
        else:
            pygame.draw.polygon(display_surf, gray, [[c+110, d-60], [c+160, d-100], [c+160, d+100], [c+110, d+60]])
        if mazePath[drawList[0][1]][drawList[0][2]][drawList[0][3]][drawList[0][4]]==1:
            pygame.draw.polygon(display_surf, black, [[c-110, d+60], [c-160, d+100], [c-160, d-100], [c-110, d-60]])
        else:
            pygame.draw.polygon(display_surf, gray, [[c-110, d+60], [c-160, d+100], [c-160, d-100], [c-110, d-60]])

        if mazePath[drawList[1][6]][drawList[1][7]][drawList[1][8]][drawList[1][9]]==1:
            pygame.draw.polygon(display_surf, black, [[c-110, d+60], [c-160, d+100], [c+160, d+100], [c+110, d+60]])
        else:
            pygame.draw.polygon(display_surf, gray, [[c-110, d+60], [c-160, d+100], [c+160, d+100], [c+110, d+60]])
        if mazePath[drawList[1][1]][drawList[1][2]][drawList[1][3]][drawList[1][4]]==1:
            pygame.draw.polygon(display_surf, black, [[c+110, d-60], [c+160, d-100], [c-160, d-100], [c-110, d-60]])
        else:
            pygame.draw.polygon(display_surf, gray, [[c+110, d-60], [c+160, d-100], [c-160, d-100], [c-110, d-60]])
        drawList=backup

        #십자가
        pygame.draw.line(display_surf, white, (400,0), (400,600), 2)
        pygame.draw.line(display_surf, white, (0,300), (800,300), 2)
        #x표시
        pn_List=[[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for x, y in pn_List:
            pygame.draw.line(display_surf, white, [a+x*110, b+y*60], [a+x*160, b+y*100], 2)

    #위치 정보
    pygame.draw.rect(display_surf, white, (310, 250, 180, 100))
    pygame.draw.rect(display_surf, black, (312, 252, 176, 96))
    font=pygame.font.Font(None, 40)
    text=font.render("POSTION", True, white)
    t=font.render((App.playerpos[0], App.playerpos[1], App.playerpos[2], App.playerpos[3]), True, white)
    display_surf.blit(text, (335, 255))
    display_surf.blit(t, (335, 300))

    #좌표 평면 정보
    i=-1
    center=[[200, 150, 0], [600, 150, 2], [200, 450, 4], [600, 450, 6]]
    pos_List=[[-10, -10], [-10, -145], [-150, -10], [120,-10], [-10, -90], [-10, 70]]
    con=["XP", "XN", "YP", "YN", "ZP", "ZN", "WP", "WN"]
    for p_x, p_y, in pos_List:
        i+=1
        for ps_x, ps_y, N in center:
            font=pygame.font.Font(None, 30)
            text=font.render(con[N+i], True, white)
            display_surf.blit(text, (ps_x+p_x, ps_y+p_y))
        if i==1:
            dis=(con[0], con[1])
            for _ in range(2):
                con.remove(con[0])
            con.extend(dis)
            i=0
            pygame.display.flip()

