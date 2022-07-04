import pygame


def enum(**enums):
    return type('Enum', (), enums)


AWParams = enum(DOUBLEBUF=pygame.DOUBLEBUF, FULLSCREEN=pygame.FULLSCREEN, RESIZABLE=pygame.RESIZABLE, NOBORDER=pygame.NOFRAME, HIDDENMODE=pygame.HIDDEN, SCALED=pygame.SCALED, OPENGL=pygame.OPENGL)
