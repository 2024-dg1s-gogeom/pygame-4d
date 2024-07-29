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
        self.size = self.weight, self.height = 800, 600
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
 
    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.maze = Maze(100)
        self.render = render.front_render 
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        keys = pygame.key.get_pressed()
        if self.render == render.front_render and keys[pygame.KSCAN_KP_ENTER]:
            self.render = render.play_render
        modifier = 1
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:# Shift key is pressed
            modifier = -1
        if keys[pygame.K_q]:
            self.maze.Update([modifier*1, 0, 0, 0])
        if keys[pygame.K_w]:
            self.maze.Update([0, modifier*1, 0, 0])
        if keys[pygame.K_e]:
            self.maze.Update([0, 0, modifier*1, 0])
        if keys[pygame.K_r]:
            self.maze.Update([0, 0, 0, modifier*1])

    def on_render(self):
        # pass
        self.render(self.font, self.maze, self._display_surf)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

