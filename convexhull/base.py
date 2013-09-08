__author__ = 'orhan'


class ConvexHullBase(object):

    def __init__(self):
        self.points = list()

    def add_point(self, p):
        self.points.append(p)

    def calculate(self):
        raise Exception('Not implemented!')