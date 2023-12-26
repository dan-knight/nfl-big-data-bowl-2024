# pyright: reportUnknownMemberType=false, reportUnknownArgumentType=false
from matplotlib.axes import Axes
import pandas as pd


def plot_players(
    ax: Axes,
    player_data: pd.DataFrame
):
    ax.scatter(player_data["x"], player_data["y"], c="white", edgecolors="black")
