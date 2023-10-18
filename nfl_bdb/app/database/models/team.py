from sqlalchemy.orm import mapped_column, Mapped

from nfl_bdb.app.database.models import Base


class Team(Base):
    __tablename__ = 'teams'

    team_id: Mapped[int] = mapped_column(primary_key=True)
    abbreviation: Mapped[str] = mapped_column()