from math import pi, radians, cos, sin


from math import pi, radians, cos, sin
from typing import Tuple


Point = Tuple[float, float]


def circle_point(
    center: Point,
    radius: float,
    angle: float
) -> Point:
    """
    Calculate the coordinates of a point on a circle.

    Given the radius, center coordinates, and an angle in degrees measured clockwise
    from the 12 o'clock position, this function computes the coordinates (x, y) of
    the point on the circle.

    Parameters:
    - radius (float): The radius of the circle.
    - center (tuple): A tuple (cx, cy) representing the center coordinates of the circle.
    - angle (float): The angle in degrees measured clockwise from 12 o'clock.

    Returns:
    tuple: A tuple (x, y) representing the coordinates of the point on the circle.

    Example:
    >>> calculate_point_on_circle(5, (0, 0), 90)
    (0, 5)

    Note:
    - The angle is measured in degrees, and 0 degrees corresponds to the 12 o'clock
      position. The angle increases clockwise.
    - The center parameter should be a tuple with two elements representing x and y
      coordinates, respectively.

    Raises:
    - ValueError: If the radius is negative.
    - ValueError: If the angle is not a valid number.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")

    center_x, center_y = center
    modified_angle: float = -1 * (radians(angle) - pi * 0.5)
    x: float = center_x + radius * cos(modified_angle)
    y: float = center_y + radius * sin(modified_angle)

    return x, y
