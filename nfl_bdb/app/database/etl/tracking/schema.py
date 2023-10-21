from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CSVTracking:
    game_id: int
    play_id: int
    player_id: Optional[int]
    player_name: Optional[str]
    team: str
    frame: int
    time: str
    jersey_number: str
    play_direction: bool
    x: float
    y: float
    speed: float
    acceleration: float
    distance: float
    orientation: Optional[float]
    direction: Optional[float]
    event: Optional[str]
