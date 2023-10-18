import datetime
from sqlalchemy.orm import mapped_column, Mapped

from nfl_bdb.app.database.models import Base


class TrackingPoint(Base):
    __tablename__ = "tracking"

    tracking_id: Mapped[int] = mapped_column(primary_key=True)
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

    event: Mapped[str] = mapped_column(nullable=True)
    