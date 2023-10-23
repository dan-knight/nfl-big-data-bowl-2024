from dataclasses import dataclass
from typing import Optional
from marshmallow import Schema, fields

from nfl_bdb.app.database.etl import fields as etl_fields


@dataclass(frozen=True)
class CSVPlayer:
    player_id: int
    height: str
    weight: int
    birth_date: Optional[str]
    name: str
    position: str
    college_name: str


class CSVPlayerSchema(Schema):
    player_id = fields.Integer(required=True, data_key="nflId")
    name = fields.String(required=True, data_key="displayName")
    height = fields.String(required=True)
    weight = fields.Integer(required=True)
    birth_date = etl_fields.NAString(required=True, data_key="birthDate")
    position = fields.String(required=True)
    college_name = fields.String(required=True, data_key="collegeName")
