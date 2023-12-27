# pyright: reportUnknownArgumentType=false, reportUnknownMemberType=false
from math import pi

import numpy as np
import pandas as pd


def circle_point(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the coordinates of a point on a circle.

    Given the radius, center coordinates, and an angle in degrees measured clockwise
    from the 12 o'clock position, this function computes the coordinates (x, y) of
    the point on the circle.
    """
    result = pd.DataFrame(index=data.index)
    result["modified_angle"] = -1 * (np.deg2rad(data["angle"]) - pi * 0.5)

    result = pd.DataFrame(
        {
            "x": data["x"] + data["length"] * np.cos(result["modified_angle"]),
            "y": data["y"] + data["length"] * np.sin(result["modified_angle"]),
        }
    )

    return result[["x", "y"]]
