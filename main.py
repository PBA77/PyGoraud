import sys

import pygame
from pygame import PixelArray

from config import X_SIZE, Y_SIZE
from helpers import Point
from triangle_engine import TriangleEngine

pygame.init()

window = pygame.display.set_mode((X_SIZE, Y_SIZE), 0, 24)
buffer: PixelArray = pygame.PixelArray(window)

engine = TriangleEngine(buffer)

while True:

  window.fill((0, 0, 0))

  engine.draw_triangle([Point(0, 0, 0), Point(600, 100, 100), Point(50, 200, 200)])

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
