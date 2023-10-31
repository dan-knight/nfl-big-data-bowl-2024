import datetime
import unittest
from typing import Any, Dict

from nfl_bdb.app.database.etl.fields import DATE_FORMAT
from nfl_bdb.app.database.etl.player.schema import CSVPlayer, CSVPlayerSchema


class TestCSVPlayerSchema(unittest.TestCase):
    def _create_csv_player_dict(self, csv_player: CSVPlayer) -> Dict[str, Any]:
        birth_date: str = (
            csv_player.birth_date.strftime(DATE_FORMAT)
            if csv_player.birth_date is not None
            else "NA"
        )

        result: Dict[str, Any] = {
            "nflId": csv_player.player_id,
            "displayName": csv_player.name,
            "position": csv_player.position,
            "height": csv_player.height,
            "weight": csv_player.weight,
            "birthDate": birth_date,
            "collegeName": csv_player.college_name,
        }

        return result

    def test__player_schema__handles_valid_values(self):
        player = CSVPlayer(
            player_id=10,
            name="Test Player",
            position="RB",
            height="5-11",
            weight=186,
            birth_date=datetime.date(1990, 10, 2),
            college_name="College",
        )

        player_dict: Dict[str, Any] = self._create_csv_player_dict(player)

        schema = CSVPlayerSchema()
        result = schema.load(player_dict)

        assert result == player

    def test__player_schema__handles_na_date(self):
        player = CSVPlayer(
            player_id=10,
            name="Test Player",
            position="RB",
            height="5-11",
            weight=186,
            birth_date=None,
            college_name="College",
        )

        player_dict: Dict[str, Any] = self._create_csv_player_dict(player)

        schema = CSVPlayerSchema()
        result = schema.load(player_dict)

        assert result == player
