from dataclasses import dataclass
from typing import Any, Mapping, Optional
from marshmallow import fields, post_load

from nfl_bdb.app.database.etl import fields as etl_fields
from nfl_bdb.app.database.etl.schema import GenericSchema


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


class CSVTrackingSchema(GenericSchema[CSVTracking]):
    game_id = fields.Integer(required=True, data_key="gameId")
    play_id = fields.Integer(required=True, data_key="playId")
    player_id = fields.Integer(required=True, data_key="nflId")
    player_name = fields.String(required=True, data_key="displayName")
    frame = fields.Integer(required=True, data_key="frameId")
    team = fields.String(required=True, data_key="club")
    time = fields.String(required=True)
    jersey_number = etl_fields.NAString(required=True, data_key="jerseyNumber")
    play_direction = fields.String(required=True)
    x = fields.Float(required=True)
    y = fields.Float(required=True)
    speed = fields.Float(required=True, data_key="s")
    acceleration = fields.Float(required=True, data_key="a")
    distance = fields.Float(required=True, data_key="dis")
    orientation = fields.Float(required=True, data_key="o")
    direction = fields.Float(required=True, data_key="dir")
    event = etl_fields.NAString(required=True)

    @post_load
    def _deserialize_tracking(
        self,
        data: Mapping[str, Any],
        **kwargs: Mapping[str, Any]
    ) -> CSVTracking:
        return CSVTracking(**data)