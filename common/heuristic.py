import math


def euclidean(vec1, vec2):
    assert len(vec1) == len(vec2)

    return math.sqrt(sum([(x1-x2)*(x1-x2) for x1, x2 in zip(vec1, vec2)]))


def manhattan(vec1, vec2):
    assert len(vec1) == len(vec2)

    return sum([math.fabs(x1 - x2) for x1, x2 in zip(vec1, vec2)])


def chebyshev(vec1, vec2):
    assert len(vec1) == len(vec2)

    return max([math.fabs(x1 - x2) for x1, x2 in zip(vec1, vec2)])