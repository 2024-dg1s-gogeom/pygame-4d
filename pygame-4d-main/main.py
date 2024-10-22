import pygame
from pygame.locals import *
from maze.maze import Maze
from maze.maze import mazePath, modeOfMaze
from maze.maze import startRmazeX, startRmazeY, startRmazeZ, startRmazeW
import render

class App:
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
            render.play_render(self.font, self.maze, self._display_surf)
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


