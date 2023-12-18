import datetime
from dataclasses import dataclass
from typing import Any, Mapping, Optional

from marshmallow import fields, post_load

from nfl_bdb.database.etl import fields as etl_fields
from nfl_bdb.database.etl.schema import GenericSchema


@dataclass(frozen=True)
class CSVPlay:
    play_id: int
    game_id: int
    ball_carrier_id: int
    ball_carrier_name: str
    play_description: str
    quarter: int
    down: int
    yards_to_go: int
    possession_team: str
    defensive_team: str
    yard_line_side: Optional[str]
    yard_line_number: int
    game_clock: datetime.time
    pre_snap_home_score: int
    pre_snap_away_score: int
    pass_result: Optional[str]
    pass_length: Optional[int]
    penalty_yards: Optional[int]
    pre_penalty_play_result: int
    play_result: int
    play_nullified_by_penalty: bool
    absolute_yard_line: int
    offense_formation: str
    defenders_in_the_box: Optional[int]
    pass_probability: Optional[float]
    pre_snap_home_team_win_probability: float
    pre_snap_away_team_win_probability: float
    home_team_win_probability_added: float
    away_team_win_probability_added: float
    expected_points: float
    expected_points_added: Optional[float]
    foul_name_1: Optional[str]
    foul_name_2: Optional[str]
    foul_player_id_1: Optional[int]
    foul_player_id_2: Optional[int]


class CSVPlaySchema(GenericSchema[CSVPlay]):
    play_id = fields.Integer(required=True, data_key="playId")
    game_id = fields.Integer(required=True, data_key="gameId")
    ball_carrier_id = fields.Integer(required=True, data_key="ballCarrierId")
    ball_carrier_name = fields.String(required=True, data_key="ballCarrierDisplayName")
    play_description = fields.String(required=True, data_key="playDescription")
    quarter = fields.Integer(required=True)
    down = fields.Integer(required=True)
    yards_to_go = fields.Integer(required=True, data_key="yardsToGo")
    possession_team = fields.String(required=True, data_key="possessionTeam")
    defensive_team = fields.String(required=True, data_key="defensiveTeam")
    yard_line_side = etl_fields.NAString(required=True, data_key="yardlineSide")
    yard_line_number = fields.Integer(required=True, data_key="yardlineNumber")
    game_clock = fields.Time(format="%M:%S", required=True, data_key="gameClock")
    pre_snap_home_score = fields.Integer(required=True, data_key="preSnapHomeScore")
    pre_snap_away_score = fields.Integer(required=True, data_key="preSnapVisitorScore")
    pass_result = fields.String(data_key="passResult", load_default=None)
    pass_length = etl_fields.NAInteger(required=True, data_key="passLength")
    penalty_yards = etl_fields.NAInteger(required=True, data_key="penaltyYards")
    pre_penalty_play_result = fields.Integer(
        required=True, data_key="prePenaltyPlayResult"
    )
    play_result = fields.Integer(required=True, data_key="playResult")
    play_nullified_by_penalty = fields.Boolean(
        required=True, data_key="playNullifiedByPenalty"
    )
    absolute_yard_line = fields.Integer(
        required=True, data_key="absoluteYardlineNumber"
    )
    offense_formation = fields.String(required=True, data_key="offenseFormation")
    defenders_in_the_box = etl_fields.NAInteger(
        required=True, data_key="defendersInTheBox"
    )
    pass_probability = etl_fields.NAFloat(required=True, data_key="passProbability")
    pre_snap_home_team_win_probability = fields.Float(
        required=True, data_key="preSnapHomeTeamWinProbability"
    )
    pre_snap_away_team_win_probability = fields.Float(
        required=True, data_key="preSnapVisitorTeamWinProbability"
    )
    home_team_win_probability_added = fields.Float(
        required=True, data_key="homeTeamWinProbabilityAdded"
    )
    away_team_win_probability_added = fields.Float(
        required=True, data_key="visitorTeamWinProbilityAdded"
    )
    expected_points = fields.Float(required=True, data_key="expectedPoints")
    expected_points_added = etl_fields.NAFloat(
        required=True, data_key="expectedPointsAdded"
    )
    foul_name_1 = etl_fields.NAString(required=True, data_key="foulName1")
    foul_name_2 = etl_fields.NAString(required=True, data_key="foulName2")
    foul_player_id_1 = etl_fields.NAInteger(required=True, data_key="foulNFLId1")
    foul_player_id_2 = etl_fields.NAInteger(required=True, data_key="foulNFLId2")

    @post_load
    def _deserialize_play(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> CSVPlay:
        return CSVPlay(**data)
