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
        self.maze = Maze(100)
        self.k = 0


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        for event in pygame.event.get():
            self.on_event(event)  # 이벤트 처리
            
            if event.type == pygame.KEYDOWN and self.render == render.front_render:  # 키가 눌렸을 때
                if event.key == pygame.K_SPACE:  # 스페이스바가 눌렸는지 확인
                    self.k += 1
            # play 끝나고 finish로 갈 때 다시 self.k = 0 으로 해야 함.
        if self.k == 0:
            self.render = render.front_render
        else:
            self.render = render.play_render
        
        ##### 플레이어 이동 알고리즘 #####
        self.playerpos = [0, 0, 0, 0] # 실제 플레이어의 좌표
        self.playerposSaved = [0, 0, 0, 0] # 이 곳으로 이동했다고 가정했을 때 플레이어의 좌표
        modifier = 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:    # SHIFT 누를 때 마다 앞 뒤 이동 방향 바뀜
            modifier *= -1
            if keys[pygame.K_q]:
                self.playerposSaved[0] += modifier * 1
            if keys[pygame.K_w]: 
                self.playerposSaved[1] += modifier * 1
            if keys[pygame.K_e]:
                self.playerposSaved[2] += modifier * 1
            if keys[pygame.K_r]:
                self.playerposSaved[3] += modifier * 1

        ##### 벽(못가는곳) 생성 알고리즘 #####
        if mazePath[self.playerpos[0]][self.playerpos[1]][self.playerpos[2]][self.playerpos[3]] == 0:
            self.playerposSaved = self.playerpos # 이동했을 때 막혀있다면 self.playerpos를 그대로 두고, 업데이트된 playerposSaved는 업데이트되기 전 좌표(self.playepos)로 변환
        else:
            self.playerpos = self.playerposSaved # 이동했을 때 막혀있지 않다면 saved된 정보를 실제 값에 업로드함으로써 이동

        ##### 맵 탈출 방지 알고리즘 #####
        if self.playerpos[0]<0 or self.playerpos[0]>19 or self.playerpos[1]<0 or self.playerpos[1]>19 or self.playerpos[2]<0 or self.playerpos[2]>19 or self.playerpos[3]<0 or self.playerpos[3]>19:
            self.playerposSaved = self.playerpos # 이동했을 때 막혀있다면 self.playerpos를 그대로 두고, 업데이트된 playerposSaved는 업데이트되기 전 좌표(self.playepos)로 변환
        else:
            self.playerpos = self.playerposSaved # 이동했을 때 막혀있지 않다면 saved된 정보를 실제 값에 업로드함으로써 이동

        ##### 벽 그거 (map.py에 옮길거) #####

    def on_render(self):
        self.render(self.font, self.maze, self._display_surf)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

