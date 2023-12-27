import unittest
from numpy.testing import assert_allclose


from nfl_bdb.utility.angle import circle_point, Point


class TestAngleUtilities(unittest.TestCase):
    def assert_coords_equal(self, a: Point, b: Point):
        assert_allclose(a, b, atol=0.001)

    def test__circle_point__handles_positive_x(self):
        center: Point = (0, 0)
        center_x, center_y = center
        radius: float = 1
        angle: float = 90

        result: Point = circle_point(center=center, angle=angle, radius=radius)
        expected_result: Point = (center_x + radius, center_y)

        self.assert_coords_equal(result, expected_result)
    
    def test__circle_point__handles_negative_x_result(self):
        center: Point = (0, 0)
        center_x, center_y = center
        radius: float = 3
        angle: float = 270

        result: Point = circle_point(center=center, angle=angle, radius=radius)
        expected_result: Point = (center_x - radius, center_y)

        self.assert_coords_equal(result, expected_result)
    
    def test__center_point__handles_positive_y(self):
        center: Point = (0, 0)
        center_x, center_y = center
        radius: float = 2.5
        angle: float = 0

        result: Point = circle_point(center=center, angle=angle, radius=radius)
        expected_result: Point = (center_x, center_y + radius)

        self.assert_coords_equal(result, expected_result)
    
    def test__circle_point__handles_negative_y_result(self):
        center: Point = (0, 0)
        center_x, center_y = center
        radius: float = 3
        angle: float = 180

        result: Point = circle_point(center=center, angle=angle, radius=radius)
        expected_result: Point = (center_x, center_y - radius)

        self.assert_coords_equal(result, expected_result)
