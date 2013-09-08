__author__ = 'orhan'

from convexhull.base import ConvexHullBase


class GrahamScan(ConvexHullBase):

    def calculate(self):
        self.bottom_right = self.get_bottom_right_point()
        sorted_list = [point for point in sorted(self.points, cmp=self.__compare_with_x_angle) if point != self.bottom_right]

        result_list = list()
        result_list.append(self.bottom_right)
        result_list.append(sorted_list[0])

        for i in xrange(1, len(sorted_list)):
            point = sorted_list[i]
            ind = len(result_list) - 2

            while self.__cross_product(result_list[ind], result_list[ind+1], point) < 0:
                result_list.pop()
                ind -= 1

            result_list.append(point)

        return result_list

    def __cross_product(self, p1, p2, p3):
        return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)

    def __compare_with_x_angle(self, p1, p2):
        a1 = self.bottom_right.angle_x(p1)
        a2 = self.bottom_right.angle_x(p2)
        if a1 > a2:
            return 1
        if a1 == a2:
            return 0
        return -1

    def get_bottom_right_point(self):
        bottom_point = self.points[0]
        for point in self.points:
            if (point.y < bottom_point.y) or (point.y == bottom_point.y and point.x > bottom_point.x):
                bottom_point = point

        return bottom_point