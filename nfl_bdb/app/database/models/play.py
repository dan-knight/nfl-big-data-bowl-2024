from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from nfl_bdb.app.database.models import Base
from nfl_bdb.app.database.models.team import Team
from nfl_bdb.app.database.models.player import Player


class Play(Base):
    __tablename__ = 'plays'

    play_id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()

    ball_carrier_id: Mapped[int] = mapped_column(ForeignKey("players.player_id"))

    quarter: Mapped[int] = mapped_column()
    game_time: Mapped[int] = mapped_column()
    down: Mapped[int] = mapped_column()

    offensive_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))

    los: Mapped[int] = mapped_column()
    los_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    yard_line: Mapped[int] = mapped_column()  # "absolute" yard line

    yards_to_go: Mapped[int] = mapped_column()
    offensive_formation: Mapped[str] = mapped_column()
    defenders_in_box: Mapped[int] = mapped_column()

    play_result: Mapped[int] = mapped_column()
    pre_penalty_play_result: Mapped[int] = mapped_column()

    pass_result: Mapped[str] = mapped_column(nullable=True)
    pass_length: Mapped[int] = mapped_column(nullable=True)

    home_score: Mapped[int] = mapped_column()
    away_score: Mapped[int] = mapped_column()

    penalty_yards: Mapped[int] = mapped_column(nullable=True)
    nullified_by_penalty: Mapped[bool] = mapped_column()

    pass_probability: Mapped[float] = mapped_column()

    home_win_probability: Mapped[float] = mapped_column()
    away_win_probability: Mapped[float] = mapped_column()

    home_win_probability_added: Mapped[float] = mapped_column()
    away_win_probability_added: Mapped[float] = mapped_column()

    expected_points: Mapped[float] = mapped_column()
    expected_points_added: Mapped[float] = mapped_column()

    foul_1: Mapped[str] = mapped_column(nullable=True)
    foul_2: Mapped[str] = mapped_column(nullable=True)

    foul_player_id_1: Mapped[Player] = mapped_column(ForeignKey("players.player_id"), nullable=True)
    foul_player_id_2: Mapped[Player] = mapped_column(ForeignKey("players.player_id"), nullable=True)
    
    ball_carrier: Mapped[Player] = relationship(Player, foreign_keys=[ball_carrier_id])
    foul_player_1: Mapped[Player] = relationship(Player, foreign_keys=[foul_player_id_1])
    foul_player_2: Mapped[Player] = relationship(Player, foreign_keys=[foul_player_id_2])
    
    offensive_team: Mapped[Team] = relationship(Team, foreign_keys=[offensive_team_id])
    los_team: Mapped[Team] = relationship(Team, foreign_keys=[los_team_id])
