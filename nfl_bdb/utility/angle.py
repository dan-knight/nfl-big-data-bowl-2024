from math import pi, radians, cos, sin


def calculate_dx(angle: float, radius: float) -> float:
    return radius * cos(-1 * (radians(angle) - pi * 0.5))


def calculate_dy(angle: float, radius: float) -> float:
    return radius * sin(-1 * (radians(angle) - pi * 0.5))
