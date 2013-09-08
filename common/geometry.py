__author__ = 'orhan'

from math import asin, sqrt, degrees


class Point:
    def __init__(self, x, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def angle_x(self, p2):
        dy = self.y - p2.y
        dx = self.x - p2.x
        h = sqrt(dy ** 2 + dx ** 2)
        if h == 0:
            return 0

        return degrees(asin(dx / h))

    def __cmp__(self, other):
        return (self.x - other.x) or (self.y - other.y) or (self.z - other.z)

    def __eq__(self, other):
        return self.__cmp__(other) == 0.0

    def __ne__(self, other):
        return self.__cmp__(other) != 0.0