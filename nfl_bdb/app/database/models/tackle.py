from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nfl_bdb.app.database.models import Base

if TYPE_CHECKING:
    from nfl_bdb.app.database.models.play import Play
    from nfl_bdb.app.database.models.player import Player


class Tackle(Base):
    __tablename__ = "tackles"

    tackle_id: Mapped[int] = mapped_column(primary_key=True)
    play_id: Mapped[int] = mapped_column(ForeignKey("plays.play_id"))
    player_id: Mapped[int] = mapped_column(ForeignKey("players.player_id"))

    tackled: Mapped[bool] = mapped_column()
    assist: Mapped[bool] = mapped_column()
    forced_fumble: Mapped[bool] = mapped_column()
    missed: Mapped[bool] = mapped_column()

    play: Mapped["Play"] = relationship()
    player: Mapped["Player"] = relationship()
