from sqlalchemy.orm import mapped_column, Mapped

from nfl_bdb.app.database.models import Base


class Play(Base):
    __tablename__ = 'plays'

    play_id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()

    # ball_carrier_id
    # ball_carrier_name (NO)

    quarter: Mapped[int] = mapped_column()
    game_time: Mapped[int] = mapped_column()
    down: Mapped[int] = mapped_column()

    # offense_team_id
    # defense_team_id

    # yard_line_side
    # yard_line_team_id
    # team_yard_line
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

    # foul_1 NULL
    # foul_2 NULL

    # foul_player_id_1 NULL
    # foul_player_id_2 NULL
