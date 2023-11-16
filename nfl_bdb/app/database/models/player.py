import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from nfl_bdb.app.database.models import Base


class Player(Base):
    __tablename__ = "players"

    player_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    position: Mapped[str] = mapped_column()
    height: Mapped[int] = mapped_column()
    weight: Mapped[int] = mapped_column()
    birth_date: Mapped[Optional[datetime.date]] = mapped_column(nullable=True)
    college: Mapped[str] = mapped_column()
