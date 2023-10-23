from dataclasses import dataclass
from typing import Optional
from marshmallow import Schema, fields

from nfl_bdb.app.database.etl import fields as etl_fields


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
    defensive_team: int
    yard_line_side: str
    yard_line_number: int
    game_clock: str
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
    defenders_in_the_box: int
    pass_probability: Optional[float]
    pre_snap_home_team_win_probability: float
    pre_snap_away_team_win_probability: float
    home_team_win_probability_added: float
    away_team_win_probability_added: float
    expected_points: float
    expected_points_added: float
    foul_name_1: Optional[str]
    foul_name_2: Optional[str]
    foul_player_id_1: Optional[int]
    foul_player_id_2: Optional[int]


class CSVPlaySchema(Schema):
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
    yard_line_side = fields.String(required=True, data_key="yardLineSide")
    yard_line_number = fields.Integer(required=True, data_key="yardLineNumber")
    game_clock = fields.String(required=True, data_key="gameClock")
    pre_snap_home_score = fields.Integer(required=True, data_key="preSnapHomeScore")
    pre_snap_away_score = fields.Integer(required=True, data_key="preSnapVisitorScore")
    pass_result = fields.String(data_key="passResult")
    pass_length = etl_fields.NAInteger(required=True, data_key="passLength")
    penalty_yards = etl_fields.NAInteger(required=True, data_key="penaltyYards")
    pre_penalty_play_result = fields.String(required=True, data_key="prePenaltyPlayResult")
    play_result = fields.Integer(required=True, data_key="playResult")
    play_nullified_by_penalty = fields.Boolean(required=True, data_key="playNullifiedByPenalty")
    absolute_yard_line = fields.Integer(required=True, data_key="absoluteYardLine")
    offense_formation = fields.String(required=True, data_key="offenseFormation")
    defenders_in_the_box = fields.Integer(required=True, data_key="defendersInTheBox")
    pass_probability = etl_fields.NAFloat(required=True, data_key="passProbability")
    pre_snap_home_team_win_probability = fields.Float(required=True, data_key="preSnapHomeTeamWinProbability")
    pre_snap_away_team_win_probability = fields.Float(required=True, data_key="preSnapVisitorTeamWinProbability")
    home_team_win_probability_added = fields.Float(required=True, data_key="homeTeamWinProbabilityAdded")
    away_team_win_probability_added = fields.Float(required=True, data_key="visitorTeamWinProbabilityAdded")
    expected_points = fields.Float(required=True, data_key="expectedPoints")
    expected_points_added = fields.Float(required=True, data_key="expectedPointsAdded")
    foul_name_1 = etl_fields.NAString(required=True, data_key="foulName1")
    foul_name_2 = etl_fields.NAString(required=True, data_key="foulName2")
    foul_player_id_1 = etl_fields.NAInteger(required=True, data_key="foulNflId1")
    foul_player_id_2 = etl_fields.NAInteger(required=True, data_key="foulNflId2")
