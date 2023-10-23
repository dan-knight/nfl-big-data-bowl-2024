from dataclasses import dataclass
from typing import Any, Mapping
from marshmallow import fields, post_load

from nfl_bdb.app.database.etl.schema import GenericSchema


@dataclass(frozen=True)
class CSVTackle:
    game_id: int
    play_id: int
    player_id: int
    tackle: bool
    assist: bool
    forced_fumble: bool
    pff_missed_tackle: bool


class CSVTackleSchema(GenericSchema[CSVTackle]):
    game_id = fields.Integer(required=True, data_key="gameId")
    play_id = fields.Integer(required=True, data_key="playId")
    player_id = fields.Integer(required=True, data_key="nflId")
    tackle = fields.Boolean(required=True)
    assist = fields.Boolean(required=True)
    forced_fumble = fields.Boolean(required=True, data_key="forcedFumble")
    pff_missed_tackle = fields.Boolean(required=True, data_key="pff_missedTackle")

    @post_load
    def _deserialize_tackle(
        self,
        data: Mapping[str, Any],
        **kwargs: Mapping[str, Any]
    ) -> CSVTackle:
        return CSVTackle(**data)
