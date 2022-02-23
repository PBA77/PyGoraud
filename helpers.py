from dataclasses import dataclass


@dataclass
class Point:
  x: int
  y: int
  z: int


def interpolator(x: list[int], y: list[list[int]]):
  assert len(x) == 2 and len(y) > 0
  dx = x[1] - x[0]
  dy = []
  yr = []
  for y_it in y:
    dy.append((y_it[1] - y_it[0]) / dx if dx > 0 else 0)
    yr.append(y_it[0])
  for xr in range(x[0], x[0] + dx):
    yield int(xr), [int(yr[i]) for i in range(len(y))]
    for i in range(len(y)):
      yr[i] += dy[i]
