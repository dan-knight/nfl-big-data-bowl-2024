from dataclasses import dataclass
from marshmallow import Schema, fields


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


class CSVGameSchema(Schema):
    game_id = fields.Integer(required=True, data_key="gameId")
    season = fields.Integer(required=True)
    week = fields.Integer(required=True)
    game_date = fields.String(required=True, data_key="gameDate")
    game_time = fields.String(required=True, data_key="gameTimeEastern")
    home_team = fields.String(required=True, data_key="homeTeamAbbr")
    away_team = fields.String(required=True, data_key="visitorTeamAbbr")
    home_score = fields.Integer(required=True, data_key="homeFinalScore")
    away_score = fields.Integer(required=True, data_key="visitorFinalScore")
