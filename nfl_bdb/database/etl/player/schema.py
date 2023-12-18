import datetime
from dataclasses import dataclass
from typing import Any, Mapping, Optional

from marshmallow import fields, post_load

from nfl_bdb.database.etl import fields as etl_fields
from nfl_bdb.database.etl.fields import DATE_FORMAT
from nfl_bdb.database.etl.schema import GenericSchema


@dataclass(frozen=True)
class CSVPlayer:
    player_id: int
    height: str
    weight: int
    birth_date: Optional[datetime.date]
    name: str
    position: str
    college_name: str


class CSVPlayerSchema(GenericSchema[CSVPlayer]):
    player_id = fields.Integer(required=True, data_key="nflId")
    name = fields.String(required=True, data_key="displayName")
    height = fields.String(required=True)
    weight = fields.Integer(required=True)
    birth_date = etl_fields.NAMultiFormatDate(
        formats=[DATE_FORMAT, "%m/%d/%Y"], required=True, data_key="birthDate"
    )
    position = fields.String(required=True)
    college_name = fields.String(required=True, data_key="collegeName")

    @post_load
    def _deserialize_player(
        self, data: Mapping[str, Any], many: bool, **kwargs: Mapping[str, Any]
    ) -> CSVPlayer:
        return CSVPlayer(**data)
