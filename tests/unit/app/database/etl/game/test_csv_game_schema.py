import datetime
from typing import Any, Dict
import unittest
from nfl_bdb.app.database.etl.fields import DATE_FORMAT, TIME_FORMAT
from nfl_bdb.app.database.etl.game.schema import CSVGame, CSVGameSchema


class TestCSVGameSchema(unittest.TestCase):
    def _create_csv_game_dict(self, csv_game: CSVGame) -> Dict[str, Any]:
        game_date: str = csv_game.game_date.strftime(DATE_FORMAT)
        game_time: str = csv_game.game_time.strftime(TIME_FORMAT)
        
        result: Dict[str, Any] = {
            "gameId": csv_game.game_id,
            "season": csv_game.season,
            "week": csv_game.week,
            "gameDate": game_date,
            "gameTimeEastern": game_time,
            "homeTeamAbbr": csv_game.home_team,
            "visitorTeamAbbr": csv_game.away_team,
            "homeFinalScore": csv_game.home_score,
            "visitorFinalScore": csv_game.away_score,
        }

        return result

    def test__game_schema__handles_valid_values(self):
        game = CSVGame(
            game_id=10,
            season=2022,
            week=3,
            game_date=datetime.date(1990, 10, 2),
            game_time=(datetime.time(1)),
            home_team="HOME",
            away_team="AWAY",
            home_score=20,
            away_score=17
        )

        game_dict: Dict[str, Any] = self._create_csv_game_dict(game)

        schema = CSVGameSchema()
        result = schema.load(game_dict)

        assert result == game
