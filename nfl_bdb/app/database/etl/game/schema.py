from dataclasses import dataclass
import datetime
from typing import Any, Mapping
from marshmallow import fields, post_load

from nfl_bdb.app.database.etl.fields import DATE_FORMAT, TIME_FORMAT
from nfl_bdb.app.database.etl.schema import GenericSchema


@dataclass(frozen=True)
class CSVGame:
    game_id: int
    season: int
    week: int
    game_date: datetime.date
    game_time: datetime.time
    home_team: str
    away_team: str
    home_score: int
    away_score: int


class CSVGameSchema(GenericSchema[CSVGame]):
    game_id = fields.Integer(required=True, data_key="gameId")
    season = fields.Integer(required=True)
    week = fields.Integer(required=True)
    game_date = fields.Date(format=DATE_FORMAT, required=True, data_key="gameDate")
    game_time = fields.Time(format=TIME_FORMAT, required=True, data_key="gameTimeEastern")
    home_team = fields.String(required=True, data_key="homeTeamAbbr")
    away_team = fields.String(required=True, data_key="visitorTeamAbbr")
    home_score = fields.Integer(required=True, data_key="homeFinalScore")
    away_score = fields.Integer(required=True, data_key="visitorFinalScore")

    @post_load
    def _deserialize_game(
        self,
        data: Mapping[str, Any],
        **kwargs: Mapping[str, Any]
    ) -> CSVGame:
        return CSVGame(**data)
