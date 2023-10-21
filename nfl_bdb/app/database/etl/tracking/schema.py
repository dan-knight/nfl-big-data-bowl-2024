from dataclasses import dataclass
from typing import Optional
from marshmallow import Schema, fields


@dataclass(frozen=True)
class CSVTracking:
    game_id: int
    play_id: int
    player_id: Optional[int]
    player_name: str
    team: str
    frame: int
    time: str
    jersey_number: str
    play_direction: str
    x: float
    y: float
    speed: float
    acceleration: float
    distance: float
    orientation: Optional[float]
    direction: Optional[float]
    event: Optional[str]


class CSVTrackingSchema(Schema):
    game_id = fields.Integer(required=True, data_key="gameId")
    play_id = fields.Integer(required=True, data_key="playId")
    player_id = fields.Integer(data_key="nflId")
    player_name = fields.String(required=True, data_key="displayName")
    frame = fields.Integer(required=True, data_key="frameId")
    team = fields.String(required=True, data_key="club")
    time = fields.String(required=True)
    jersey_number = fields.String(data_key="jerseyNumber")
    play_direction = fields.String(required=True)
    x = fields.Float(required=True)
    y = fields.Float(required=True)
    speed = fields.Float(required=True, data_key="s")
    acceleration = fields.Float(required=True, data_key="a")
    distance = fields.Float(required=True, data_key="dis")
    orientation = fields.Float(data_key="o")
    direction = fields.Float(data_key="dir")
    event = fields.String()
