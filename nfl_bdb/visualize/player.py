# pyright: reportUnknownMemberType=false, reportUnknownArgumentType=false
from typing import Iterable, List

import pandas as pd
from matplotlib.animation import FuncAnimation
from matplotlib.artist import Artist
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
from matplotlib.figure import Figure
from matplotlib.quiver import Quiver

from nfl_bdb.utility.angle import circle_point


def plot_players(ax: Axes, player_data: pd.DataFrame) -> Axes:
    plot_player_points(ax, player_data)

    if "orientation" in player_data.columns:
        player_data = pd.concat(
            [player_data, _get_dx_dy(player_data)],
            axis=1
        )
        plot_player_orientation(ax, player_data)
    
    return ax


def animate_players(fig: Figure, ax: Axes, player_data: pd.DataFrame) -> FuncAnimation:
    frame_data: pd.DataFrame = player_data.reorder_levels(
        order=["frame", "player_id"]
    ).sort_index(level="frame")
    frames: List[int] = player_data.index.unique("frame").tolist()

    first_frame: int = frames.pop(0)
    scatter = plot_player_points(ax, frame_data.loc[[first_frame], ["x", "y"]])

    if "orientation" in frame_data.columns:
        frame_data = pd.concat(
            [frame_data, _get_dx_dy(frame_data)],
            axis=1
        )
        arrows = plot_player_orientation(ax, frame_data.loc[[first_frame], :])

    def animate(frame: int) -> Iterable[Artist]:
        scatter.set_offsets(frame_data.loc[[frame], ["x", "y"]])

        if arrows:
            arrows.set_offsets(frame_data.loc[[frame], ["x", "y"]])
            arrows.set_UVC(frame_data.loc[[frame], "dx"], frame_data.loc[[frame], "dy"])

        return [scatter, arrows]

    return FuncAnimation(
        fig, animate, frames=frame_data.index.unique("frame"), interval=100
    )


def plot_player_points(ax: Axes, player_data: pd.DataFrame) -> PathCollection:
    return ax.scatter(
        player_data["x"],
        player_data["y"],
        c="white",
        edgecolors="black"
    )


def _get_dx_dy(player_data: pd.DataFrame) -> pd.DataFrame:
    dx_dy: pd.DataFrame = circle_point(
        pd.DataFrame(
            {"x": 0, "y": 0, "angle": player_data["orientation"], "length": 0.05}
        )
    ).rename(columns={"x": "dx", "y": "dy"})
    return dx_dy


def plot_player_orientation(ax: Axes, player_data: pd.DataFrame) -> Quiver:
    return ax.quiver(
        player_data["x"],
        player_data["y"],
        player_data["dx"],
        player_data["dy"],
        scale=2.5,
        width=3,
        headlength=1,
        headaxislength=1,
        headwidth=1,
        minlength=0,
    )
