from dataclasses import dataclass


@dataclass(frozen=True)
class CSVGame:
    game_id: int
    season: int
    week: int
    game_date: str
    game_time: str
    home_team: str
    away_team: str
    home_score: int
    away_score: int
