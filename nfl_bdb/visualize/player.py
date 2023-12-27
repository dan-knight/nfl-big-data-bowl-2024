# pyright: reportUnknownMemberType=false, reportUnknownArgumentType=false
from matplotlib.axes import Axes
import pandas as pd

from nfl_bdb.utility.angle import circle_point


def plot_players(
    ax: Axes,
    player_data: pd.DataFrame
):
    ax.scatter(player_data["x"], player_data["y"], c="white", edgecolors="black")
    

def plot_player_orientation(ax: Axes, player_data: pd.DataFrame):
    dx_dy: pd.DataFrame = circle_point(
        pd.DataFrame({
            "x": 0,
            "y": 0,
            "angle": player_data["orientation"],
            "length": 0.05
        })
    )
    ax.quiver(
        player_data["x"],
        player_data["y"],
        dx_dy["x"],
        dx_dy["y"],
        scale=2.5,
        width=3,
        headlength=1,
        headaxislength=1,
        headwidth=1,
        minlength=0
    )
