from itertools import chain

from pygame.pixelarray import PixelArray

from config import X_SIZE, Y_SIZE
from helpers import interpolator, Point


class TriangleEngine:
  _x2 = [0] * X_SIZE
  _zz = [0] * Y_SIZE

  def __init__(self, buffer: PixelArray):
    self._buffer = buffer

  @staticmethod
  def _interpolate_xz(idx_1: int, idx_2: int, pts: list[Point]):
    return interpolator([pts[idx_1].y, pts[idx_2].y], [[pts[idx_1].x, pts[idx_2].x], [pts[idx_1].z, pts[idx_2].z]])

  def _h_line(self, points: list[Point]):
    assert len(points) == 2
    points.sort(key=lambda it: it.x)
    for x, z in interpolator([points[0].x, points[1].x], [[points[0].z, points[1].z]]):
      if 0 < x < X_SIZE and 0 < points[0].y < Y_SIZE:
        self._buffer[x, points[0].y] = (z[0], z[0], z[0])

  def draw_triangle(self, pts: list[Point]):
    assert len(pts) == 3
    pts.sort(key=lambda it: it.y)
    for y, x in self._interpolate_xz(0, 2, pts):
      self._x2[y], self._zz[y] = x[0], x[1]
    for y, (x, z) in chain(self._interpolate_xz(0, 1, pts), self._interpolate_xz(1, 2, pts)):
      self._h_line([Point(x, y, z), Point(self._x2[y], y, self._zz[y])])
