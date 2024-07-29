import pygame
from pygame.locals import *
from maze.maze import Maze
from scene.front import Front
from scene.play import Play
from scene.finish import Finish

scene = {
    'front': Front(),
    'play': Play(),
    'finish': Finish(),
}

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.maze = Maze(100)
        self.scene = scene['front']
        # self.scene.font = pygame.font.Font(None, 36)
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        # Goto play at front scene if key ENTER is pressed
        if self.scene.name() == 'front' and event.type == pygame.KSCAN_KP_ENTER:
            self.scene = scene['play']
        # Goto front at play scene if key ESC is pressed
        if self.scene.name() == 'play' and event.type == pygame.KSCAN_ESCAPE:
            self.scene = scene['front']
        # Goto front at finish scene if key ENTER is pressed
        if self.scene.name() == 'finish' and event.type == pygame.KSCAN_KP_ENTER:
            self.scene = scene['front']

    def on_loop(self):
        keys = pygame.key.get_pressed()
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
        self.scene.render(self.maze, self._display_surf)

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

