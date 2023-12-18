from sqlalchemy.orm import Mapped, mapped_column

from nfl_bdb.database.models import Base


class Team(Base):
    __tablename__ = "teams"

    team_id: Mapped[int] = mapped_column(primary_key=True)
    abbreviation: Mapped[str] = mapped_column()
