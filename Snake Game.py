import pygame
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((640,640))
nomx = (random.randint(0,640) // 10) * 10
nomy = (random.randint(0,640) // 10) * 10
snakex = (random.randint(0,640) // 10) * 10
snakey = (random.randint(0,640) // 10) * 10
down = 0
up = 0
down = 0
right = 0
left = 0
death = 0
score = 0
replay = 0
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()
snakelist = []
snakelist.append([snakex, snakey])
def text_boi():
  fontobj = pygame.font.SysFont("freesans", 32)
  msgobj = fontobj.render(score, False, red)
  screen.blit(msgobj, (630, 630))
while True:
  clock.tick(17)
  screen.fill(black)
  pygame.draw.rect(screen, red, (nomx, nomy, 10, 10),0)
  snakelist.pop(0)
  snakelist.append([snakex, snakey])
  for n in snakelist:
    pygame.draw.rect(screen, green, n + [10, 10])
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    elif event.type == KEYDOWN:
      if event.key == K_DOWN:
        if up == 0:
          down = 1
          up = 0
          left = 0
          right = 0
      elif event.key == K_UP:
        if down == 0:
          up = 1
          down = 0
          left = 0
          right = 0
      elif event.key == K_LEFT:
        if right == 0:
          left = 1
          right = 0
          up = 0
          down = 0
      elif event.key == K_RIGHT:
        if left == 0:
          right = 1
          left = 0
          up = 0
          down = 0
  if down == 1:
    snakey = snakey + 10
  elif up == 1:
    snakey = snakey - 10
  elif left == 1:
    snakex = snakex - 10
  elif right == 1:
    snakex = snakex + 10
  if snakex < 0:
    snakex = 640
  elif snakex > 640:
    snakex = 0
  elif snakey < 0:
    snakey = 640
  elif snakey > 640:
    snakey = 0
  if snakex == nomx and snakey == nomy:
    nomx = (random.randint(0,640) // 10) * 10
    nomy = (random.randint(0,640) // 10) * 10
    score = score + 1
    snakelist.append([snakex, snakey])
  pygame.display.update()
    
