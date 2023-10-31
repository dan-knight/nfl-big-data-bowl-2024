from typing import Any, Dict
import unittest

from nfl_bdb.app.database.etl.tackle.schema import CSVTackle, CSVTackleSchema


class TestCSVTackleSchema(unittest.TestCase):
    def _create_csv_tackle_dict(self, csv_tackle: CSVTackle) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "gameId": csv_tackle.game_id,
            "playId": csv_tackle.play_id,
            "nflId": csv_tackle.player_id,
            "tackle": csv_tackle.tackle,
            "assist": csv_tackle.assist,
            "forcedFumble": csv_tackle.forced_fumble,
            "pff_missedTackle": csv_tackle.pff_missed_tackle
        }

        return result

    def test__tackle_schema__handles_valid_values(self):
        tackle = CSVTackle(
            game_id=10,
            play_id=1000,
            player_id=1,
            tackle=True,
            assist=True,
            forced_fumble=False,
            pff_missed_tackle=False
        )

        tackle_dict: Dict[str, Any] = self._create_csv_tackle_dict(tackle)

        schema = CSVTackleSchema()
        result = schema.load(tackle_dict)

        assert result == tackle
