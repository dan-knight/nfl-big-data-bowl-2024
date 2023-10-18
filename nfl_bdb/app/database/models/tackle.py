from sqlalchemy.orm import mapped_column, Mapped

from nfl_bdb.app.database.models import Base


class Tackle(Base):
    __tablename__ = "tackles"

    tackle_id: Mapped[int] = mapped_column(primary_key=True)
    
    tackled: Mapped[bool] = mapped_column()
    assist: Mapped[bool] = mapped_column()
    forced_fumble: Mapped[bool] = mapped_column()
    missed: Mapped[bool] = mapped_column()