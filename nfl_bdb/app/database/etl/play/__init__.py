from typing import Dict, List

from nfl_bdb.app.database.etl.factory import ETLFactory, FactoryTeamIndex
from nfl_bdb.app.database.etl.play.schema import CSVPlay
from nfl_bdb.app.database.models.play import Play as DBPlay
from nfl_bdb.app.database.models.team import Team as DBTeam


class PlayFactory(ETLFactory, FactoryTeamIndex):
    def __init__(self, team_index: Dict[str, DBTeam]):
        self._team_index: Dict[str, DBTeam] = team_index

    def transform_play(self, csv_play: CSVPlay) -> DBPlay:
        game_time = self._parse_game_clock_time(csv_play.game_clock)
        los_team: DBTeam = self._get_team(csv_play.yard_line_side)

        return DBPlay(
            play_id=csv_play.play_id,
            game_id=csv_play.game_id,
            description=csv_play.play_description,
            ball_carrier_id=csv_play.ball_carrier_id,
            quarter=csv_play.quarter,
            game_time=game_time,
            offensive_team_id=csv_play.possession_team,
            yard_line=csv_play.absolute_yard_line,
            los=csv_play.yard_line_number,
            los_team=los_team,
            yards_to_go=csv_play.yards_to_go,
            offensive_formation=csv_play.offense_formation,
            defenders_in_box=csv_play.defenders_in_the_box,
            play_result=csv_play.play_result,
            pre_penalty_play_result=csv_play.pre_penalty_play_result,
            pass_result=csv_play.pass_result,
            pass_length=csv_play.pass_length,
            home_score=csv_play.pre_snap_home_score,
            away_score=csv_play.pre_snap_away_score,
            penalty_yards=csv_play.penalty_yards,
            nullified_by_penalty=csv_play.play_nullified_by_penalty,
            pass_probability=csv_play.pass_probability,
            home_win_probability=csv_play.pre_snap_home_team_win_probability,
            away_win_probability=csv_play.pre_snap_away_team_win_probability,
            home_win_probability_added=csv_play.home_team_win_probability_added,
            away_win_probability_added=csv_play.away_team_win_probability_added,
            expected_points=csv_play.expected_points,
            expected_points_added=csv_play.expected_points_added,
            foul_1=csv_play.foul_name_1,
            foul_player_id_1=csv_play.foul_player_id_1,
            foul_2=csv_play.foul_name_2,
            foul_player_id_2=csv_play.foul_player_id_2,
        )

    def _parse_game_clock_time(self, csv_time: str) -> int:
        split_time: List[str] = csv_time.split(":")

        invalid_format_error = ValueError(f'Invalid game clock format "{csv_time}"')
        if not len(split_time) == 2:
            raise invalid_format_error

        try:
            (minutes, seconds) = int(split_time[0]), int(split_time[1])
        except TypeError:
            raise invalid_format_error

        return minutes * 60 + seconds
