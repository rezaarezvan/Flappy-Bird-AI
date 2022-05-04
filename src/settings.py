from dependencies import pygame,os

pygame.font.init()

WIN_WIDTH = 550
WIN_HEIGHT = 800

GEN = 0

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))) , pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))) , pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BACKGROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "background.png")))

STAT_FONT = pygame.font.SysFont('Arial', 40)