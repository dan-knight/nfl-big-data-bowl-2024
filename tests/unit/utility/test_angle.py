import unittest
from numpy import float64
from pandas.testing import assert_frame_equal
import pandas as pd


from nfl_bdb.utility.angle import circle_point


class TestAngleUtilities(unittest.TestCase):
    def assert_coords_equal(self, a: pd.DataFrame, b: pd.DataFrame):
        assert_frame_equal(a, b, atol=0.001)

    def test__circle_point__handles_positive_x(self):
        n: int = 10
        radius: float = 1
        angle: float = 90
        center_x: float = 0
        center_y: float = 0
    
        input_points = pd.DataFrame({
            "x": [center_x] * n,
            "y": [center_y] * n,
            "length": [radius] * n,
            "angle": [angle] * n
        })

        result: pd.DataFrame = circle_point(input_points)
        expected_result = pd.DataFrame({
            "x": pd.Series([center_x + radius] * n, dtype=float64),
            "y": pd.Series([center_y] * n, dtype=float64)
        })

        self.assert_coords_equal(result, expected_result)
    
    def test__circle_point__handles_negative_x_result(self):
        n: int = 9
        center_x: float = 0
        center_y: float = 0
        radius: float = 3
        angle: float = 270
    
        input_points = pd.DataFrame({
            "x": [center_x] * n,
            "y": [center_y] * n,
            "length": [radius] * n,
            "angle": [angle] * n
        })

        result: pd.DataFrame = circle_point(input_points)
        expected_result = pd.DataFrame({
            "x": pd.Series([center_x - radius] * n, dtype=float64),
            "y": pd.Series([center_y] * n, dtype=float64)
        })

        self.assert_coords_equal(result, expected_result)
    
    def test__center_point__handles_positive_y(self):
        n: int = 8
        center_x: float = 0
        center_y: float = 0
        radius: float = 2.5
        angle: float = 0

        input_points = pd.DataFrame({
            "x": [center_x] * n,
            "y": [center_y] * n,
            "length": [radius] * n,
            "angle": [angle] * n
        })

        result: pd.DataFrame = circle_point(input_points)
        expected_result = pd.DataFrame({
            "x": pd.Series([center_x] * n, dtype=float64),
            "y": pd.Series([center_y + radius] * n, dtype=float64)
        })

        self.assert_coords_equal(result, expected_result)
    
    def test__circle_point__handles_negative_y_result(self):
        n: int = 7
        center_x: float = 0
        center_y: float = 0
        radius: float = 3
        angle: float = 180

        input_points = pd.DataFrame({
            "x": [center_x] * n,
            "y": [center_y] * n,
            "length": [radius] * n,
            "angle": [angle] * n
        })

        result: pd.DataFrame = circle_point(input_points)
        expected_result = pd.DataFrame({
            "x": pd.Series([center_x] * n, dtype=float64),
            "y": pd.Series([center_y - radius] * n, dtype=float64)
        })

        self.assert_coords_equal(result, expected_result)
