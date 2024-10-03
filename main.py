import pygame
from pygame.locals import *
from maze.maze import Maze
from maze.maze import mazePath
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
        self.playerpos = [0, 0, 0, 0] # 실제 플레이어의 좌표
        self.playerposSaved = [0, 0, 0, 0] # 이 곳으로 이동했다고 가정했을 때 플레이어의 좌표
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
                    self.playerposSaved[0] += self.modifier * 1
                if event.key == pygame.K_w: 
                    self.playerposSaved[1] += self.modifier * 1
                if event.key == pygame.K_e:
                    self.playerposSaved[2] += self.modifier * 1
                if event.key == pygame.K_r:
                    self.playerposSaved[3] += self.modifier * 1

            ##### 벽(못가는곳) 생성 알고리즘 #####
            if mazePath[self.playerposSaved[0]][self.playerposSaved[1]][self.playerposSaved[2]][self.playerposSaved[3]] == 0:
                self.playerposSaved = self.playerpos

            ##### 맵 탈출 방지 #####
            elif self.playerposSaved[0]<0 or self.playerposSaved[0]>19 or self.playerposSaved[1]<0 or self.playerposSaved[1]>19 or self.playerposSaved[2]<0 or self.playerposSaved[2]>19 or self.playerposSaved[3]<0 or self.playerposSaved[3]>19:
                self.playerposSaved = self.playerpos

            else:
                self.playerpos = self.playerposSaved

            print(f"{self.playerpos}, {self.playerposSaved}, {mazePath[self.playerposSaved[0]][self.playerposSaved[1]][self.playerposSaved[2]][self.playerposSaved[3]]}")

            ### 게임 끝 ###
            if mazePath[self.playerpos[0]][self.playerpos[1]][self.playerpos[2]][self.playerpos[3]] == 3:
                self.k = 2

    def on_render(self):
        if self.k == 0:
            render.front_render(self.font, self.maze, self._display_surf)
        elif self.k == 1:
            render.play_render(self.font, self.maze, self._display_surf)
        elif self.k == 2:
            render.finish_render(self.font, self.maze, self._display_surf)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            self.on_render()
            self.on_loop()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

