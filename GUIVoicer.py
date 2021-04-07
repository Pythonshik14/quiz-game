import pygame
from ctypes import windll
import ctypes

pygame.init()

def create_window(size):
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    window = pygame.display.get_wm_info()['window']
    windll.user32.SetWindowPos(window, -1, widthMonitor() // 2 - 25, 0, 0, 0, 0x0001)
    return screen

def widthMonitor():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0)


def func_():

    screen = create_window((200, 25))
    fonty = pygame.font.Font(None, 36)
    text = fonty.render("  Voice AS Leila ", True, (0, 0, 0))


    clock = pygame.time.Clock()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    screen.blit(text, (2, 2))
    clock.tick(30)
    pygame.display.update()