import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nfl_bdb.app.database.models import Base
from nfl_bdb.app.database.models.play import Play
from nfl_bdb.app.database.models.player import Player


class TrackingPoint(Base):
    __tablename__ = "tracking"

    tracking_id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.player_id"))
    play_id: Mapped[int] = mapped_column(ForeignKey("plays.play_id"))
    frame: Mapped[int] = mapped_column()

    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()

    speed: Mapped[float] = mapped_column()
    acceleration: Mapped[float] = mapped_column()
    direction: Mapped[float] = mapped_column()
    orientation: Mapped[float] = mapped_column()

    distance_traveled: Mapped[float] = mapped_column()

    timestamp: Mapped[datetime.datetime] = mapped_column()
    jersey: Mapped[int] = mapped_column()

    event: Mapped[Optional[str]] = mapped_column(nullable=True)

    player: Mapped[Player] = relationship()
    play: Mapped[Play] = relationship()
