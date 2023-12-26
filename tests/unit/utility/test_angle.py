import unittest

from nfl_bdb.utility.angle import calculate_dx, calculate_dy


class TestAngleUtilities(unittest.TestCase):
    def test__calculate_dx__handles_valid_angle(self):
        radius: float = 1
        angle: float = 90

        result: float = calculate_dx(angle=angle, radius=radius)
        expected_result: float = radius

        self.assertAlmostEqual(result, expected_result)
    
    def test__calculate_dx__handles_negative_result(self):
        radius: float = 3
        angle: float = 270

        result: float = calculate_dx(angle=angle, radius=radius)
        expected_result: float = -1 * radius

        self.assertAlmostEqual(result, expected_result)
    
    def test__calculate_dy__handles_valid_angle(self):
        radius: float = 2.5
        angle: float = 0

        result: float = calculate_dy(angle=angle, radius=radius)
        expected_result: float = radius

        self.assertAlmostEqual(result, expected_result)
    
    def test__calculate_dy__handles_negative_result(self):
        radius: float = 3
        angle: float = 180

        result: float = calculate_dy(angle=angle, radius=radius)
        expected_result: float = -1 * radius

        self.assertAlmostEqual(result, expected_result)
