import datetime
from sqlalchemy.orm import mapped_column, Mapped

from nfl_bdb.app.database.models import Base


class Game(Base):
    __tablename__ = 'games'

    game_id: Mapped[int] = mapped_column(primary_key=True)
    kickoff_time: Mapped[datetime.date] = mapped_column()
    home_score: Mapped[int] = mapped_column()
    away_score: Mapped[int] = mapped_column()
