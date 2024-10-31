import pygame
from pygame.locals import *
from map import show_map
def front_render(font, maze, display_surf):
    basicFont = pygame.font.SysFont(None, 30, False, False)
    titleFont = pygame.font.SysFont(None, 50, False, True)
    display_surf.fill((0, 0, 0))

    titleStart = titleFont.render("Tap SPACE BAR to Start", True, (255, 255, 255))
    titleTutoQ = basicFont.render("Q: Move in the x-axis", True, (255, 255, 255))
    titleTutoW = basicFont.render("W: Move in the y-axis", True, (255, 255, 255))
    titleTutoE = basicFont.render("E: Move in the z-axis", True, (255, 255, 255))
    titleTutoR = basicFont.render("R: Move in the w-axis", True, (255, 255, 255))
    titleTutoShift = basicFont.render("SHIFT: Switching forward / backward", True, (255, 255, 255))

    display_surf.blit(titleTutoQ, (160, 180))
    display_surf.blit(titleTutoW, (160, 210))
    display_surf.blit(titleTutoE, (160, 240))
    display_surf.blit(titleTutoR, (160, 270))
    display_surf.blit(titleTutoShift, (160, 300))
    display_surf.blit(titleStart, (160, 350))

    pygame.display.flip()

def play_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    pygame.draw.line(display_surf, (255, 255, 255), (400,0), (400,600), 2)
    pygame.draw.line(display_surf, (255, 255, 255), (0,300), (800,300), 2)  
    show_map(display_surf)
    pygame.display.flip()

def finish_render(font, maze, display_surf):
    display_surf.fill((0, 0, 0))
    ending = font.render("You WON !!", True, (255, 255, 255))
    display_surf.blit(ending, (210, 232))
    goingback = font.render("Tap ESC to end game", True, (255, 255, 255))
    display_surf.blit(goingback, (210, 282))
    pygame.display.flip()

