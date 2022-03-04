"""Unit testing for Python Fundamentals Final Project"""
# Ashwini Balachandra
import unittest
from shapes import Point, Circle


# Helper functions - use these for data verification when appropriate.
def point_data(point):
    """Return tuple of Point data for comparison."""
    return (point.x, point.y)


def circle_data(circle):
    """Return tuple of Circle data for comparison."""
    return ((circle.center.x, circle.center.y), circle.radius)


class PointTests(unittest.TestCase):
    def test_p1_create_point_no_data(self):
        """P-1. Create a Point with no arguments."""
        # Create a tuple of what the answer from point_data should be
        expected = (0, 0)
        # Create a default Point instance.
        point = Point()
        # Verify that the data of the new Point instance is correct.
        self.assertEqual(point_data(point), expected)

    def test_p2_create_point_with_data(self):
        """P-2. Create a Point with values."""
        expected = (2, 3)
        point = Point(2, 3)
        self.assertEqual(point_data(point), expected)

    def test_p3_point_modification(self):
        """P-3. Verify modification of x, y works."""
        expected = (-1, 5)
        point = Point()
        point.x, point.y = -1, 5
        self.assertEqual(point_data(point), expected)

    def test_p4_point_iterable(self):
        """P-4. Verify Point is iterable."""
        expected = (2, 3)
        point = Point(2, 3)
        # To be iterable, we should be able to "unpack" it.
        x, y = point
        self.assertEqual((x, y), expected)
        # Because it is not an iterator, it can be unpacked more than once.
        j, k = point
        self.assertEqual((j, k), expected)

    def test_p4a_point_not_iterator(self):
        """P-4a. Verify point is not an iterator"""
        point = Point(2, 3)
        x = iter(point)
        # Make sure that iter(point) does not return self.
        self.assertIs(x == point, False)
        # We should not be able to call next() on a Point instance.
        with self.assertRaises(TypeError):
            next(point)

    def test_p5_magnitude(self):
        """P-5. Verify Point magnitude property."""
        expected = 3.605551275463989
        point = Point(2, 3)
        self.assertEqual(point.magnitude, expected)

    def test_p6_magnitude_changes(self):
        """P-6. Verify magnitude property changes after Point changed."""
        expected = 5
        point = Point(-1, 6)
        point.x, point.y = 3, 4
        self.assertEqual(point.magnitude, expected)

    def test_p7_distance(self):
        """P-7. Verify distance between two Point objects."""
        expected = 5
        point1 = Point(2, 3)
        point2 = Point(5, 7)
        self.assertEqual(point1.distance(point2), expected)

    def test_p8_point_addition(self):
        """P-8. Verify Point addition."""
        expected1 = (2, 3)
        expected2 = (4, 5)
        expected3 = (6, 8)
        point1 = Point(2, 3)
        point2 = Point(4, 5)
        point3 = point1 + point2
        # Ensure original points unchanged
        self.assertEqual(point_data(point1), expected1)
        self.assertEqual(point_data(point2), expected2)
        # Verify new point is correct
        self.assertEqual(point_data(point3), expected3)

    def test_p8a_point_plus_equal_addition(self):
        """P-8a. Verify Point += mutating addition."""
        expected = (6, 8)
        point1 = Point(2, 3)
        # Save the id to make sure it doesn't change.
        id1 = id(point1)
        point2 = Point(4, 5)
        # Add using +=
        point1 += point2
        self.assertEqual(point_data(point1), expected)
        # Verify point2 has not changed
        expected = (4, 5)
        self.assertEqual(point_data(point2), expected)
        # Verify that point1 is the same object
        self.assertEqual(id(point1), id1)

    def test_p9_point_str(self):
        """P-9. Verify Point str result."""
        expected = "Point at (2, 3)"
        point = Point(2, 3)
        self.assertEqual(str(point), expected)

    def test_p10_point_repr(self):
        """P-10. Verify Point repr result."""
        expected = "Point(x=2, y=3)"
        point = Point(2, 3)
        self.assertEqual(repr(point), expected)

    # Remaining Point tests go here

    def test_p11_create_point_from_tuple(self):
        """P-11. Create a Point using from_tuple."""
        # Test point = Point.from_tuple(loc)
        # where loc is a tuple
        # Make sure data is correct.
        expected = (2, 3)
        loc = 2, 3
        point = Point.from_tuple(loc)
        self.assertEqual(point_data(point), expected)

    def test_p12_error_point_from_tuple_no_args(self):
        """P-12. Verify error when using from_tuple with no arguments"""
        # Test that Point.from_tuple() raises an error
        # NOT with try/except; use unittest.
        with self.assertRaises(TypeError):
            Point.from_tuple()

    def test_p13_point_mod_loc_from_tuple(self):
        """P-13. Verify mod of x, y using loc_from_tuple."""
        # Test point.loc_from_tuple(loc)
        # when point is an existing Point and loc is a tuple.
        # Make sure data is correct.
        expected = (5, 6)
        point = Point(3, 4)
        point.loc_from_tuple((5, 6))
        self.assertEqual(point_data(point), expected)

    def test_p14_point_mod_loc_from_tuple_no_args(self):
        """P-14. Verify error when using loc_from_tuple with no arguments."""
        # Create a Point instance and test that using loc_from_tuple
        # on it raises an error.
        # NOT with try/except; use unittest.
        point = Point(3, 4)
        with self.assertRaises(TypeError):
            point.loc_from_tuple()

    def test_p15_scalar_mult_right(self):
        """P-15. Verify Point multiplied with scalar."""
        # Test point2 = point1 * 3
        # where point1 is an existing Point instance.
        # Make sure that point1 is not modified.
        expected1 = (2, 3)
        expected2 = (6, 9)
        point1 = Point(2, 3)
        point2 = point1 * 3
        # Ensure original points unchanged
        self.assertEqual(point_data(point1), expected1)
        # Verify new point is correct
        self.assertEqual(point_data(point2), expected2)

    def test_p16_scalar_mult_left(self):
        """P-16. Verify scalar multiplied with Point."""
        # Test point2 = 3 * point1
        # where point1 is an existing Point instance.
        # Make sure that point1 is not modified.
        expected1 = (4, 5)
        expected2 = (12, 15)
        point1 = Point(4, 5)
        point2 = 3 * point1
        # Ensure original points unchanged
        self.assertEqual(point_data(point1), expected1)
        # Verify new point is correct
        self.assertEqual(point_data(point2), expected2)

    def test_p17_scalar_mult_plus_equal(self):
        """P-17. Verify Point *= mutating multiply with scalar."""
        # Test point1 *= 3
        # where point1 is an existing Point instance.
        # Make sure that point1 is modified (not a new Point).
        expected1 = (6, 9)
        point1 = Point(2, 3)
        # Save the id to make sure it doesn't change.
        id1 = id(point1)
        point1 *= 3
        # Verify point1 is correct
        self.assertEqual(point_data(point1), expected1)
        # Verify that point1 is the same object
        self.assertEqual(id(point1), id1)


class CircleTests(unittest.TestCase):
    def test_c0_circle_point_objects_different(self):
        """C-0. Make sure Circle centers are different objects for default."""
        # In other words, they should have the same VALUES,
        # But NOT be the same objects.
        circle1 = Circle()
        circle2 = Circle()
        # Make sure they are not the same exact objects.
        self.assertIsNot(circle1.center, circle2.center)
        # But they should have the same data values.
        self.assertEqual(circle_data(circle1), circle_data(circle2))

    def test_c1_create_no_input(self):
        """C-1. Create Circle with no arguments."""
        # Create a tuple of what the answer from circle_data should be
        expected = ((0, 0), 1)
        circle = Circle()
        self.assertEqual(circle_data(circle), expected)

    def test_c2_create_only_point_input(self):
        """C-2. Create Circle with Point but no radius."""
        expected = ((2, 3), 1)
        circle = Circle(center=Point(2, 3))
        self.assertEqual(circle_data(circle), expected)
        # Also make sure the circle's center is the same as the point input.
        point = Point(2, 3)
        point_id = id(point)
        circle = Circle(center=point)
        self.assertEqual(circle_data(circle), expected)
        self.assertEqual(point_id, id(circle.center))

    def test_c3_create_only_radius_input(self):
        """C-3. Create Circle with radius but no Point."""
        expected = ((0, 0), 2.5)
        circle = Circle(radius=2.5)
        self.assertEqual(circle_data(circle), expected)
        # Make sure radius=0 works (edge case of Circles)
        expected = ((0, 0), 0)
        circle = Circle(radius=0)
        self.assertEqual(circle_data(circle), expected)

    def test_c4_create_point_and_radius_input(self):
        """C-4. Create Circle with Point and radius."""
        expected = ((2, 3), 1.5)
        circle = Circle(center=Point(2, 3), radius=1.5)
        self.assertEqual(circle_data(circle), expected)

    def test_c5_create_no_keywords(self):
        """C-5. Create Circle without keywords."""
        expected = ((2, 3), 1.5)
        circle = Circle(Point(2, 3), 1.5)
        self.assertEqual(circle_data(circle), expected)

    def test_c5a_move_center(self):
        """C-5A. Verify moving center Point of Circle works."""
        expected = ((6, 2), 1.5)
        point = Point(2, 3)
        circle = Circle(point, 1.5)
        point.x = 6
        point.y = 2
        self.assertEqual(circle_data(circle), expected)

    def test_c6_area(self):
        """C-6. Verify area property."""
        expected = 12.566370614359172
        circle = Circle(radius=2)
        self.assertEqual(circle.area, expected)

    # Remaining Circle tests go here

    def test_c7_change_radius(self):
        """C-7. Verify radius attribute change works."""
        # Create circle instance
        # Test circle.radius = some new number
        expected = ((4, 5), 3.5)
        point = Point(4, 5)
        circle = Circle(point, 1.5)
        circle.radius = 3.5
        self.assertEqual(circle_data(circle), expected)

    def test_c8_area_changed(self):
        """C-8. Verify area changes correctly when radius changes."""
        # Create circle instance
        # Set circle.radius = some new number
        # Verify the circle.area changes correctly.
        expected1 = 3.141592653589793
        expected2 = 12.566370614359172
        circle = Circle(Point(4, 5), 1)
        self.assertEqual(circle.area, expected1)
        circle.radius = 2
        self.assertEqual(circle.area, expected2)

    def test_c9_change_center(self):
        """C-9. Verify center attribute change works."""
        # Create circle instance
        # Test circle.center = point
        # where point is a Point instance with different data
        # Verify circle instance has correct center
        expected = ((5, 4), 3)
        point1 = Point(y=5, x=8)
        circle = Circle(point1, 3)
        circle.center = Point(y=4, x=5)
        self.assertEqual(circle_data(circle), expected)

    def test_c10_illegal_center_creation(self):
        """C-10. Verify error if center is not a Point on creation."""
        # Test something like Circle(center = 1)
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        with self.assertRaises(TypeError):
            Circle(center=(1, 1), radius=3)

    def test_c11_illegal_center_modification(self):
        """C-11. Verify error if changing center to something not a Point."""
        # Test something like circle.center = 2
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        circle = Circle(Point(1, 1), 2)
        with self.assertRaises(TypeError):
            circle.center = (3, 1)

    def test_c12_diameter(self):
        """C-12. Verify diameter property works."""
        # Create a Circle instance and verify that
        # circle.diameter is correct.
        # also:
        # Verify diameter changes with a radius change
        # technically this should be another test function
        expected = 8
        circle = Circle(radius=4)
        self.assertEqual(circle.diameter, expected)

    def test_c13_diameter_changes(self):
        """C-13. Verify diameter changes works."""
        # Create a Circle instance; change circle.diameter
        # Verify that the circle's radius changed correctly
        expected = 3.5
        circle = Circle(radius=8)
        circle.diameter = 7
        self.assertEqual(circle.radius, expected)

    def test_c14_create_negative_radius(self):
        """C-14. Verify error when radius < 0."""
        # Test something like Circle(center=Point(2, 3), radius=-2)
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        with self.assertRaises(ValueError):
            Circle(Point(1, 3), -6)

    def test_c15_change_negative_radius(self):
        """C-15. Verify error when radius changes to be < 0."""
        # Test changing circle.radius = -2
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        circle = Circle(Point(2, 5), 3)
        with self.assertRaises(ValueError):
            circle.radius = -2

    def test_c16_change_negative_diameter(self):
        """C-16. Verify error when diameter changes to be < 0."""
        # Test changing circle.diameter = -2
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        circle = Circle(Point(2, 4), 3)
        with self.assertRaises(ValueError):
            circle.diameter = -2

    def test_c17_circle_addition(self):
        """C-17. Verify Circle addition."""
        # Create 2 circles, add them together, make sure
        # the new circle is correct and first 2 circles unchanged.
        expected1 = ((3, 1), 1)
        expected2 = ((1, 3), 3)
        expected3 = ((4, 4), 4)
        circle1 = Circle(Point(3, 1), 1)
        circle2 = Circle(Point(1, 3), 3)
        circle3 = circle1 + circle2
        # Ensure original circles unchanged
        self.assertEqual(circle_data(circle1), expected1)
        self.assertEqual(circle_data(circle2), expected2)
        # Verify new circle is correct
        self.assertEqual(circle_data(circle3), expected3)

    def test_c17a_circle_plus_equal_addition(self):
        """C-17a. Verify Circle += mutating addition."""
        # Create 2 circles, then do circle1 += circle2
        # Make sure circle1 is correct and is the same object.
        # Make sure circle2 is unchanged.
        expected1 = ((4, 4), 4)
        expected2 = ((1, 3), 3)
        circle1 = Circle(Point(3, 1), 1)
        # Save the id to make sure it doesn't change.
        id1 = id(circle1)
        circle2 = Circle(Point(1, 3), 3)
        # Add using +=
        circle1 += circle2
        self.assertEqual(circle_data(circle1), expected1)
        # Verify that point1 is the same object
        self.assertEqual(id(circle1), id1)
        # Verify circle2 has not changed
        self.assertEqual(circle_data(circle2), expected2)

    def test_c18_circle_str(self):
        """C-18. Verify Circle str result."""
        # Test str(circle) result is exactly like instructions.
        expected = "Circle with center at (8, 3) and radius 2"
        circle = Circle(Point(8, 3), 2)
        self.assertEqual(str(circle), expected)

    def test_c19_circle_repr(self):
        """C-19. Verify Circle repr result."""
        # Test repr(circle) is exactly like instructions.
        expected = "Circle(center=Point(4, 3), radius=5)"
        circle = Circle(Point(4, 3), 5)
        self.assertEqual(repr(circle), expected)

    def test_c20_circle_create_from_tuple(self):
        """C-20. Test circle creation using from_tuple."""
        # Test something like Circle.from_tuple(center=(3, 4), radius=2)
        expected = ((7, 4), 9)
        center_point = 7, 4
        circle = Circle.from_tuple(center_point, 9)
        self.assertEqual(circle_data(circle), expected)

    def test_c21_circle_create_from_tuple_no_args(self):
        """C-21. Verify error using Circle.from_tuple with no arguments."""
        # Create a circle with Circle.from_tuple()
        # Verify an error occurs.
        with self.assertRaises(TypeError):
            Circle.from_tuple()

    def test_c22_circle_create_from_tuple_only_tuple(self):
        """C-22. Test circle creation using from_tuple with only tuple."""
        # Test something like Circle.from_tuple(center=(3, 4))
        expected = ((3, 4), 1)
        center_point = 3, 4
        circle = Circle.from_tuple(center_point)
        self.assertEqual(circle_data(circle), expected)

    def test_c23_circle_modify_center_from_tuple(self):
        """C-23. Test circle modify with center_from_tuple method."""
        # Create a circle and a tuple t
        # Test circle.center_from_tuple(t)
        expected = ((3, 4), 6)
        circle = Circle(Point(2, 2), 6)
        new_center = 3, 4
        circle.center_from_tuple(new_center)
        self.assertEqual(circle_data(circle), expected)

    def test_c24_circle_modify_center_from_tuple_no_args(self):
        """C-24. Verify error using center_from_tuple with no arguments."""
        # Create a circle and do circle.center_from_tuple()
        # Verify an error is raised.
        circle = Circle(Point(2, 5), 3)
        with self.assertRaises(TypeError):
            circle.center_from_tuple()


if __name__ == "__main__":
    unittest.main()

