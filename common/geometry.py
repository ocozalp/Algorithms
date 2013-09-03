__author__ = 'orhan'

from math import asin, sqrt, degrees

class Point:
    def __init__(self, x, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def angleX(self, p2):
        dy = self.y - p2.y
        dx = self.x - p2.x
        h = sqrt(dy ** 2 + dx ** 2)
        if h == 0:
            return 0

        return degrees(asin(dy / h))