import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from nfl_bdb.app.database.models import Base

from nfl_bdb.app.database.models.team import Team


class Game(Base):
    __tablename__ = 'games'

    game_id: Mapped[int] = mapped_column(primary_key=True)
    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    
    kickoff_time: Mapped[datetime.date] = mapped_column()
    home_score: Mapped[int] = mapped_column()
    away_score: Mapped[int] = mapped_column()

    home_team: Mapped[Team] = relationship(Team, foreign_keys=[home_team_id])
    away_team: Mapped[Team] = relationship(Team, foreign_keys=[away_team_id])
