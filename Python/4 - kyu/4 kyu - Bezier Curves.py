# https://www.codewars.com/kata/bezier-curves/train/python
# My solution
from abc import ABCMeta, abstractmethod

class Segment(metaclass=ABCMeta):
    @property
    @abstractmethod
    def control_points(self):
        pass
    @abstractmethod
    def point_at(self, t):
        pass
    @abstractmethod
    def sub_segment(self, t):
        pass
    def _median_points(self, t, P):
        equation = lambda t, P: (1-t) * P[0] + t * P[1]
        median   = lambda t, P0,P1: [equation(t, [P0[0], P1[0]]), equation(t, [P0[1], P1[1]])]
        P = list(zip(P[::2], P[1::2]))
        M = []
        for P0,P1 in zip(P[:-1], P[1:]):
            M += median(t, P0, P1)
        return M

class Line(Segment):
    def __init__(self, *coords):
        self._control_points = coords
    @property
    def control_points(self):
        return self._control_points
    def point_at(self, t):
        return self._median_points(t, self._control_points)
    def sub_segment(self, t):
        P = self._control_points
        x, y = self.point_at(t)
        return Line(P[0], P[1], x, y)

class Quad(Segment):
    def __init__(self, *coords):
        self._control_points = coords
    @property
    def control_points(self):
        return self._control_points
    def point_at(self, t):
        P = self._control_points
        equation = lambda t, P: (1-t)**2 * P[0] + 2 * (1-t) * t * P[1] + t**2 * P[2]
        return [equation(t, P[::2]), equation(t, P[1::2])] 
    def sub_segment(self, t):
        P = self._control_points
        R = [P[0], P[1]]
        M = [P]
        while len(M[-1]) > 2:
            M += [self._median_points(t, M[-1])]
            R += [M[-1][0], M[-1][1]]
        return Quad(*R)

class Cubic(Segment):
    def __init__(self, *coords):
        self._control_points = coords
    @property
    def control_points(self):
        return self._control_points
    def point_at(self, t):
        P = self._control_points
        equation = lambda t, P: (1-t)**3 * P[0] + 3 * (1-t)**2 * t * P[1] + 3 * (1-t) * t**2 * P[2] + t**3 * P[3]
        return [equation(t, P[::2]), equation(t, P[1::2])]
    def sub_segment(self, t):
        P = self._control_points
        R = [P[0], P[1]]
        M = [P]
        while len(M[-1]) > 2:
            M += [self._median_points(t, M[-1])]
            R += [M[-1][0], M[-1][1]]
        return Cubic(*R)

# ...
class Segment:  # Instead of an abstract class, make it the implementation for all three subclasses
    def __init__(self, *coords):
        self.control_points = coords  # IMHO a getter/setter is overkill here

    def control_points_at(self, t):  # Helper function
        p = self.control_points
        result = []
        while p:
            result.extend(p[:2])
            p = [v + (p[i+2] - v) * t for i, v in enumerate(p[:-2])]
        return result

    def point_at(self, t):
        return tuple(self.control_points_at(t)[-2:])

    def sub_segment(self, t):
        return self.__class__(*self.control_points_at(t))

class Line(Segment): pass
class Quad(Segment): pass
class Cubic(Segment): pass