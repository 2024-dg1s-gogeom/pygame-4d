import pygame
from pygame.locals import *
from maze.maze import Maze
from maze.maze import mazePath, modeOfMaze
from maze.maze import startRmazeX, startRmazeY, startRmazeZ, startRmazeW
import render
class App:
    def show_map(self, display_surf):
        px = self.playerpos[0]
        py = self.playerpos[1]
        pz = self.playerpos[2]
        pw = self.playerpos[3]
        drawList = [
            [200, 150, px+1, py, pz, pw, px-1, py, pz, pw, 1], 
            [600, 150, px, py+1, pz, pw, px, py-1, pz, pw, 2], 
            [200, 450, px, py, pz+1, pw, px, py, pz-1, pw, 3], 
            [600, 450, px, py, pz, pw+1, px, py, pz, pw-1, 4]
            ]
        
        backup=drawList
        gray = (180, 180, 180)
        black= (0, 0, 0)
        white= (255, 255, 255)
        for a, b, i1, i2, i3, i4, i5, i6, i7, i8, vi in drawList:
            c,d=backup[vi-1][0], backup[vi-1][1]
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
                di=(drawList[0])
                drawList.remove(drawList[0])
                drawList.append(di)
            if mazePath[drawList[0][6]][drawList[0][7]][drawList[0][8]][drawList[0][9]]==1:
                pygame.draw.polygon(display_surf, black, [[c+110, d-60], [c+160, d-100], [c+160, d+100], [c+110, d+60]])
            else:
                pygame.draw.polygon(display_surf, gray, [[c+110, d-60], [c+160, d-100], [c+160, d+100], [c+110, d+60]])
            if mazePath[drawList[0][2]][drawList[0][3]][drawList[0][4]][drawList[0][5]]==1:
                pygame.draw.polygon(display_surf, black, [[c-110, d+60], [c-160, d+100], [c-160, d-100], [c-110, d-60]])
            else:
                pygame.draw.polygon(display_surf, gray, [[c-110, d+60], [c-160, d+100], [c-160, d-100], [c-110, d-60]])

            if mazePath[drawList[1][6]][drawList[1][7]][drawList[1][8]][drawList[1][9]]==1:
                pygame.draw.polygon(display_surf, black, [[c-110, d+60], [c-160, d+100], [c+160, d+100], [c+110, d+60]])
            else:
                pygame.draw.polygon(display_surf, gray, [[c-110, d+60], [c-160, d+100], [c+160, d+100], [c+110, d+60]])
            if mazePath[drawList[1][2]][drawList[1][3]][drawList[1][4]][drawList[1][5]]==1:
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
                pygame.draw.line(display_surf, white, [c+x*110, d+y*60], [c+x*160, d+y*100], 2)
            #프레임

         #위치 정보
        pygame.draw.rect(display_surf, white, (310, 250, 180, 100))
        pygame.draw.rect(display_surf, black, (312, 252, 176, 96))
        font=pygame.font.Font(None, 40)
        text=font.render("POSTION", True, white)
        display_surf.blit(text, (335, 255))

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
                con.remove(con[0])
                con.remove(con[0])
                con.extend(dis)
                i=-1
                pygame.display.flip()
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 600
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.maze = Maze()
        self.k = 0
        if modeOfMaze == 'r':
            self.playerpos = [startRmazeX, startRmazeY, startRmazeZ, startRmazeW]
        elif modeOfMaze == 's':
            self.playerpos = [0,0,0,0]
        self.modifier = 1

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        for event in pygame.event.get():
            self.on_event(event)  # 이벤트 처리
            
            ### 게임 시작 ###
            if event.type == pygame.KEYDOWN and self.k == 0:  # 키가 눌렸을 때
                if event.key == pygame.K_SPACE:  # 스페이스바가 눌렸는지 확인
                    self.k = 1

            ### 게임 진행 ###
            if event.type == pygame.KEYDOWN and self.k == 1:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:    # SHIFT 누를 때 앞 뒤 이동 방향 바뀜
                    self.modifier *= -1
                if event.key == pygame.K_q:
                    self.playerpos[0] += self.modifier * 1 # modifier에 1 곱함 -> 앞으로 전진
                if event.key == pygame.K_w: 
                    self.playerpos[1] += self.modifier * 1
                if event.key == pygame.K_e:
                    self.playerpos[2] += self.modifier * 1
                if event.key == pygame.K_r:
                    self.playerpos[3] += self.modifier * 1

            if  ( 
                    mazePath[self.playerpos[0]][self.playerpos[1]][self.playerpos[2]][self.playerpos[3]] == 0 or # 벽 생성
                    self.playerpos[0]<0 or self.playerpos[0]>20 or # 맵 못 빠져나가도록
                    self.playerpos[1]<0 or self.playerpos[1]>20 or 
                    self.playerpos[2]<0 or self.playerpos[2]>20 or 
                    self.playerpos[3]<0 or self.playerpos[3]>20
                ):

                if event.type == pygame.KEYDOWN and self.k == 1: 
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:    
                        self.modifier *= -1
                    if event.key == pygame.K_q:
                        self.playerpos[0] += self.modifier * -1 # modifier에 -1 곱함 -> 뒤로 돌아오도록
                    if event.key == pygame.K_w: 
                        self.playerpos[1] += self.modifier * -1
                    if event.key == pygame.K_e:
                        self.playerpos[2] += self.modifier * -1
                    if event.key == pygame.K_r:
                        self.playerpos[3] += self.modifier * -1

            print(f"{self.playerpos},{mazePath[self.playerpos[0]][self.playerpos[1]][self.playerpos[2]][self.playerpos[3]]}")
            # 이거는 플레이어 좌표 확인용. 나중에 가운데에 플레이어 좌표 띄우고 난 후에는 지워야함
            
            ### 게임 끝 ###
            if mazePath[self.playerpos[0]][self.playerpos[1]][self.playerpos[2]][self.playerpos[3]] == 3:
                self.k = 2
            
            if event.type == pygame.KEYDOWN and self.k == 2:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    def on_render(self):
        if self.k == 0:
            render.front_render(self.font, self.maze, self._display_surf)
        elif self.k == 1:
            render.play_render(self.font, self.maze, self, self._display_surf)
        elif self.k == 2:
            render.finish_render(self.font, self.maze, self._display_surf)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            self.on_render()
            self.on_loop()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()



