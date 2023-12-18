import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nfl_bdb.database.models import Base
from nfl_bdb.database.models.team import Team

if TYPE_CHECKING:
    from nfl_bdb.database.models.play import Play


class Game(Base):
    __tablename__ = "games"

    game_id: Mapped[int] = mapped_column(primary_key=True)
    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))

    kickoff_time: Mapped[datetime.date] = mapped_column()
    home_score: Mapped[int] = mapped_column()
    away_score: Mapped[int] = mapped_column()

    home_team: Mapped[Team] = relationship(Team, foreign_keys=[home_team_id])
    away_team: Mapped[Team] = relationship(Team, foreign_keys=[away_team_id])
    plays: Mapped[List["Play"]] = relationship("Play", back_populates="game")
