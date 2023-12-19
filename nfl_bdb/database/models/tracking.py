import datetime
from typing import Optional

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nfl_bdb.database.models import Base
from nfl_bdb.database.models.play import Play
from nfl_bdb.database.models.player import Player


class TrackingPoint(Base):
    __tablename__ = "tracking"

    tracking_id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("players.player_id"), nullable=True
    )
    play_id: Mapped[int] = mapped_column(ForeignKey("plays.play_id"), index=True)
    frame: Mapped[int] = mapped_column()

    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()

    speed: Mapped[float] = mapped_column()
    acceleration: Mapped[float] = mapped_column()
    direction: Mapped[bool] = mapped_column()
    orientation: Mapped[Optional[float]] = mapped_column(nullable=True)

    distance_traveled: Mapped[float] = mapped_column()

    timestamp: Mapped[datetime.datetime] = mapped_column()
    jersey: Mapped[Optional[str]] = mapped_column(nullable=True)

    event: Mapped[Optional[str]] = mapped_column(nullable=True)

    player: Mapped[Optional[Player]] = relationship()
    play: Mapped[Play] = relationship()

    __table_args__ = (
        UniqueConstraint("play_id", "player_id", "frame", name="tracking_UQ1"),
    )
