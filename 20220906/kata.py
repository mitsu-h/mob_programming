class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def diff_point(self, other):
        return (self.__x-other.__x, self.__y-other.__y)

def manhattan_distance(p1, p2):
    x_diff, y_diff = p1.diff_point(p2)
    return abs(x_diff) + abs(y_diff)