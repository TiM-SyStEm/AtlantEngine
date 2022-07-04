import pygame
from pygame.locals import *
from  Atlant.AWParams import *


class AWindow:
    def __init__(self, title, iconPath=None, params=None, xSize=640, ySize=480, xPos=None, yPos=None):
        pygame.init()
        pygame.display.set_mode((xSize, ySize), params)
        pygame.display.set_caption(title)
        if iconPath != None:
            img = pygame.image.load(iconPath)
            pygame.display.set_icon(img)