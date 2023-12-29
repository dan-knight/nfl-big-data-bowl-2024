# pyright: reportUnknownMemberType=false, reportUnknownArgumentType=false
from typing import Iterable, List
from matplotlib.animation import FuncAnimation
from matplotlib.artist import Artist
from matplotlib.collections import PathCollection
from matplotlib.figure import Figure
from matplotlib.quiver import Quiver
import pandas as pd
from matplotlib.axes import Axes

from nfl_bdb.utility.angle import circle_point


def plot_players(ax: Axes, player_data: pd.DataFrame) -> PathCollection:
    return ax.scatter(player_data["x"], player_data["y"], c="white", edgecolors="black")


def plot_player_orientation(ax: Axes, player_data: pd.DataFrame) -> Quiver:
    dx_dy: pd.DataFrame = circle_point(
        pd.DataFrame(
            {"x": 0, "y": 0, "angle": player_data["orientation"], "length": 0.05}
        )
    )
    return ax.quiver(
        player_data["x"],
        player_data["y"],
        dx_dy["x"],
        dx_dy["y"],
        scale=2.5,
        width=3,
        headlength=1,
        headaxislength=1,
        headwidth=1,
        minlength=0,
    )


def animate_players(
    fig: Figure,
    ax: Axes,
    player_data: pd.DataFrame
) -> FuncAnimation:
    frame_data: pd.DataFrame = player_data.reorder_levels(order=["frame", "player_id"]).sort_index(level="frame")
    frames: List[int] = player_data.index.unique("frame").tolist()

    scatter = plot_players(ax, frame_data.loc[[frames.pop(0)], ["x", "y"]])
    def animate(frame: int) -> Iterable[Artist]:
        scatter.set_offsets(frame_data.loc[[frame], ["x", "y"]])
        return [scatter]

    return FuncAnimation(
        fig,
        animate,
        frames=frame_data.index.unique("frame"),
        interval=100
    )
