from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CSVPlay:
    play_id: int
    game_id: int
    ball_carrier_id: int
    ball_carrier_name: str
    play_description: str
    quarter: int
    down: int
    yards_to_go: int
    possession_team: str
    defensive_team: int
    yard_line_side: str
    yard_line_number: int
    game_clock: str
    pre_snap_home_score: int
    pre_snap_away_score: int
    pass_result: Optional[str]
    pass_length: Optional[int]
    penalty_yards: Optional[int]
    pre_penalty_play_result: int
    play_result: int
    play_nullified_by_penalty: bool
    absolute_yard_line: int
    offense_formation: str
    defenders_in_the_box: int
    pass_probability: Optional[float]
    pre_snap_home_team_win_probability: float
    pre_snap_away_team_win_probability: float
    home_team_win_probability_added: float
    away_team_win_probability_added: float
    expected_points: float
    expected_points_added: float
    foul_name_1: Optional[str]
    foul_name_2: Optional[str]
    foul_player_id_1: Optional[int]
    foul_player_id_2: Optional[int]
