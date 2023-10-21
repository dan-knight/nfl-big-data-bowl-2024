from dataclasses import dataclass
from marshmallow import Schema, fields


@dataclass(frozen=True)
class CSVTackle:
    game_id: int
    play_id: int
    player_id: int
    tackle: bool
    assist: bool
    forced_fumble: bool
    pff_missed_tackle: bool


class CSVTackleSchema(Schema):
    game_id = fields.Integer(required=True, data_key="gameId")
    play_id = fields.Integer(required=True, data_key="playId")
    player_id = fields.Integer(required=True, data_key="nflId")
    tackle = fields.Boolean(required=True)
    assist = fields.Boolean(required=True)
    forced_fumble = fields.Boolean(required=True, data_key="forcedFumble")
    pff_missed_tackle = fields.Boolean(required=True, data_key="pff_missedTackle")
