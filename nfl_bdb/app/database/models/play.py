from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nfl_bdb.app.database.models import Base
from nfl_bdb.app.database.models.player import Player
from nfl_bdb.app.database.models.team import Team

if TYPE_CHECKING:
    from nfl_bdb.app.database.models.game import Game


class Play(Base):
    __tablename__ = "plays"

    play_id: Mapped[int] = mapped_column(primary_key=True)
    ingame_play_id: Mapped[int] = mapped_column()
    game_id: Mapped[int] = mapped_column(ForeignKey("games.game_id"))
    description: Mapped[str] = mapped_column()

    ball_carrier_id: Mapped[int] = mapped_column(ForeignKey("players.player_id"))

    quarter: Mapped[int] = mapped_column()
    game_time: Mapped[int] = mapped_column()
    down: Mapped[int] = mapped_column()

    offensive_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))

    los: Mapped[int] = mapped_column()
    los_team_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("teams.team_id"), nullable=True
    )
    yard_line: Mapped[int] = mapped_column()  # "absolute" yard line

    yards_to_go: Mapped[int] = mapped_column()
    offensive_formation: Mapped[str] = mapped_column()
    defenders_in_box: Mapped[int] = mapped_column(nullable=True)

    play_result: Mapped[int] = mapped_column()
    pre_penalty_play_result: Mapped[int] = mapped_column()

    pass_result: Mapped[Optional[str]] = mapped_column(nullable=True)
    pass_length: Mapped[Optional[int]] = mapped_column(nullable=True)

    home_score: Mapped[int] = mapped_column()
    away_score: Mapped[int] = mapped_column()

    penalty_yards: Mapped[Optional[int]] = mapped_column(nullable=True)
    nullified_by_penalty: Mapped[bool] = mapped_column()

    pass_probability: Mapped[Optional[float]] = mapped_column(nullable=True)

    home_win_probability: Mapped[float] = mapped_column()
    away_win_probability: Mapped[float] = mapped_column()

    home_win_probability_added: Mapped[float] = mapped_column()
    away_win_probability_added: Mapped[float] = mapped_column()

    expected_points: Mapped[float] = mapped_column()
    expected_points_added: Mapped[Optional[float]] = mapped_column(nullable=True)

    foul_1: Mapped[Optional[str]] = mapped_column(nullable=True)
    foul_2: Mapped[Optional[str]] = mapped_column(nullable=True)

    foul_player_id_1: Mapped[Optional[int]] = mapped_column(
        ForeignKey("players.player_id"), nullable=True
    )
    foul_player_id_2: Mapped[Optional[int]] = mapped_column(
        ForeignKey("players.player_id"), nullable=True
    )

    game: Mapped["Game"] = relationship("Game", back_populates="plays")
    ball_carrier: Mapped[Player] = relationship(Player, foreign_keys=[ball_carrier_id])
    foul_player_1: Mapped[Optional[Player]] = relationship(
        Player, foreign_keys=[foul_player_id_1]
    )
    foul_player_2: Mapped[Optional[Player]] = relationship(
        Player, foreign_keys=[foul_player_id_2]
    )

    offensive_team: Mapped[Team] = relationship(Team, foreign_keys=[offensive_team_id])
    los_team: Mapped[Team] = relationship(Team, foreign_keys=[los_team_id])
