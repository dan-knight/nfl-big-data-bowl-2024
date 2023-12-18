import datetime
import unittest
from typing import Any, Dict

from nfl_bdb.database.etl.play.schema import CSVPlay, CSVPlaySchema


class TestCSVPlaySchema(unittest.TestCase):
    def _create_csv_play_dict(self, csv_play: CSVPlay) -> Dict[str, Any]:
        game_clock: str = csv_play.game_clock.strftime("%-M:%S")
        yard_line_side: str = (
            csv_play.yard_line_side if csv_play.yard_line_side is not None else "NA"
        )
        pass_length: str | int = (
            csv_play.pass_length if csv_play.pass_length is not None else "NA"
        )
        penalty_yards: str | int = (
            csv_play.penalty_yards if csv_play.penalty_yards is not None else "NA"
        )
        defenders: str | int = (
            csv_play.defenders_in_the_box
            if csv_play.defenders_in_the_box is not None
            else "NA"
        )
        pass_probability: str | float = (
            csv_play.pass_probability if csv_play.pass_probability is not None else "NA"
        )
        expected_points_added: str | float = (
            csv_play.expected_points_added
            if csv_play.expected_points_added is not None
            else "NA"
        )
        foul_name_1: str = (
            csv_play.foul_name_1 if csv_play.foul_name_1 is not None else "NA"
        )
        foul_name_2: str = (
            csv_play.foul_name_2 if csv_play.foul_name_2 is not None else "NA"
        )
        foul_id_1: int | str = (
            csv_play.foul_player_id_1 if csv_play.foul_player_id_1 is not None else "NA"
        )
        foul_id_2: int | str = (
            csv_play.foul_player_id_2 if csv_play.foul_player_id_2 is not None else "NA"
        )

        result: Dict[str, Any] = {
            "playId": csv_play.play_id,
            "gameId": csv_play.game_id,
            "ballCarrierId": csv_play.ball_carrier_id,
            "ballCarrierDisplayName": csv_play.ball_carrier_name,
            "playDescription": csv_play.play_description,
            "quarter": csv_play.quarter,
            "down": csv_play.down,
            "yardsToGo": csv_play.yards_to_go,
            "possessionTeam": csv_play.possession_team,
            "defensiveTeam": csv_play.defensive_team,
            "yardlineSide": yard_line_side,
            "yardlineNumber": csv_play.yard_line_number,
            "gameClock": game_clock,
            "preSnapHomeScore": csv_play.pre_snap_home_score,
            "preSnapVisitorScore": csv_play.pre_snap_away_score,
            "passResult": csv_play.pass_result,
            "passLength": pass_length,
            "penaltyYards": penalty_yards,
            "prePenaltyPlayResult": csv_play.pre_penalty_play_result,
            "playResult": csv_play.play_result,
            "playNullifiedByPenalty": csv_play.play_nullified_by_penalty,
            "absoluteYardlineNumber": csv_play.absolute_yard_line,
            "offenseFormation": csv_play.offense_formation,
            "defendersInTheBox": defenders,
            "passProbability": pass_probability,
            "preSnapHomeTeamWinProbability": csv_play.pre_snap_home_team_win_probability,
            "preSnapVisitorTeamWinProbability": csv_play.pre_snap_away_team_win_probability,
            "homeTeamWinProbabilityAdded": csv_play.home_team_win_probability_added,
            "visitorTeamWinProbilityAdded": csv_play.away_team_win_probability_added,
            "expectedPoints": csv_play.expected_points,
            "expectedPointsAdded": expected_points_added,
            "foulName1": foul_name_1,
            "foulName2": foul_name_2,
            "foulNFLId1": foul_id_1,
            "foulNFLId2": foul_id_2,
        }

        return result

    def test__play_schema__handles_valid_values(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_yard_line_side(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side=None,
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=10,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_null_pass_result(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result=None,
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_pass_length(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=None,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_penalty_yards(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=None,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_defenders(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=None,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_pass_probability(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=None,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_expected_points_added(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.32,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=None,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_foul_name_1(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1=None,
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_foul_name_2(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2=None,
            foul_player_id_1=19,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_foul_player_id_1(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=None,
            foul_player_id_2=90,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play

    def test__play_schema__handles_na_foul_player_id_2(self):
        play = CSVPlay(
            play_id=1902,
            game_id=36,
            ball_carrier_id=189,
            ball_carrier_name="Josh Jacobs",
            play_description="Description",
            quarter=3,
            down=1,
            yards_to_go=10,
            possession_team="LV",
            defensive_team="DEN",
            yard_line_side="LV",
            yard_line_number=25,
            game_clock=datetime.time(minute=3, second=12),
            pre_snap_home_score=10,
            pre_snap_away_score=3,
            pass_result="C",
            pass_length=12,
            penalty_yards=-5,
            pre_penalty_play_result=12,
            play_result=-5,
            play_nullified_by_penalty=True,
            absolute_yard_line=25,
            offense_formation="PISTOL",
            defenders_in_the_box=5,
            pass_probability=0.45,
            pre_snap_home_team_win_probability=0.65,
            pre_snap_away_team_win_probability=0.35,
            home_team_win_probability_added=-0.01,
            away_team_win_probability_added=0.01,
            expected_points=0.65,
            expected_points_added=-0.3,
            foul_name_1="Offensive Holding",
            foul_name_2="Unnecessary Roughness",
            foul_player_id_1=81,
            foul_player_id_2=None,
        )

        play_dict: Dict[str, Any] = self._create_csv_play_dict(play)

        schema = CSVPlaySchema()
        result = schema.load(play_dict)

        assert result == play
