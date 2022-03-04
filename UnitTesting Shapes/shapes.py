"""Python Fundamentals Final Project - shapes module."""
# Ashwini Balachandra
import math


class Point:
    """Two-Dimensional Point(x, y)"""

    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return "Point at ({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, other):
        """Return the distance of between the points."""
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def __add__(self, other):
        """Return a new Point object"""
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __iadd__(self, other):
        """Return a new Point object"""
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __mul__(self, num):
        """Return a new Point object"""
        x = self.x * num
        y = self.y * num
        return Point(x, y)

    def __rmul__(self, num):
        """Return a new Point object"""
        x = self.x * num
        y = self.y * num
        return Point(x, y)

    def __imul__(self, num):
        """Return a new Point object"""
        self.x = self.x * num
        self.y = self.y * num
        return self

    def loc_from_tuple(self, coords):
        """Updates a Point object"""
        self.x, self.y = coords

    @classmethod
    def from_tuple(cls, coords):
        x, y = coords
        return cls(x, y)


class Circle(Point):
    """Circle(center, radius) where center is a Point instance"""

    def __init__(self, center=None, radius=1):
        """Circle initializer"""
        Point.__init__(self, center)
        if center is None:
            center = Point(0, 0)
        self.center = center
        self.radius = radius
        if not isinstance(center, Point):
            raise TypeError("The center must be a Point!")

    @property
    def center(self):
        """Return the center of the Circle"""
        return self._center

    @center.setter
    def center(self, center):
        """Return the center."""
        if not isinstance(center, Point):
            raise TypeError("The center must be a Point!")
        self._center = center

    @property
    def radius(self):
        """Return the radius of the Circle"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Return the radius."""
        if radius < 0:
            raise ValueError("The radius cannot be negative!")
        self._radius = radius

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    def __str__(self):
        """Convert Python objects into string"""
        return "Circle with center at ({0}, {1}) and radius {2}".format(
            self.center.x, self.center.y, self.radius
        )

    def __repr__(self):
        """Printable representation of the given object"""
        return "Circle(center=Point({0}, {1}), radius={2})".format(
            self.center.x, self.center.y, self.radius
        )

    def __add__(self, other):
        return Circle(
            Point(self.center.x + other.center.x, self.center.y +
                  other.center.y),
            self.radius + other.radius,
        )

    def __iadd__(self, other):
        """Return a new Circle object"""
        self.center.x = self.center.x + other.center.x
        self.center.y = self.center.y + other.center.y
        self.radius = self.radius + other.radius
        return self

    def center_from_tuple(self, center):
        """Updates a center from tuple"""
        self.center.x, self.center.y = center
        return self

    @classmethod
    def from_tuple(cls, center, radius=1):
        x, y = center
        return cls(Point(x, y), radius)
