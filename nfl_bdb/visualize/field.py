# pyright: reportUnknownMemberType=false
from matplotlib.axes import Axes
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle


def setup_field(ax: Axes):
    ax.set_facecolor("green")
    ax.set_xticks([])
    ax.set_yticks([])

    ax.plot([0, 120], [0, 0], c="white")
    ax.plot([0, 120], [53.5, 53.3], c="white")

    ax.add_collection(PatchCollection(
        [
            Rectangle((i, 0), width=10, height=53.3)
            for i in (0, 110)
        ],
        facecolor="white"
    ))

    for i in range(0, 121, 10):
        ax.plot([i, i], [0, 53.3], c="white")
