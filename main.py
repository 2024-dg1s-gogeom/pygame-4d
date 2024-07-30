import pygame
from pygame.locals import *
from maze.maze import Maze
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
        if self.k == 0:
            self.render = render.front_render
        else:
            self.render = render.play_render
    
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

