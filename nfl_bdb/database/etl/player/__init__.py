from typing import List

from nfl_bdb.database.etl.factory import ETLFactory
from nfl_bdb.database.etl.player.schema import CSVPlayer
from nfl_bdb.database.models.player import Player as DBPlayer


class PlayerFactory(ETLFactory):
    def transform_player(self, csv_player: CSVPlayer) -> DBPlayer:
        height: int = self._parse_csv_height(csv_player.height)

        db_player = DBPlayer(
            player_id=csv_player.player_id,
            name=csv_player.name,
            position=csv_player.position,
            height=height,
            weight=csv_player.weight,
            birth_date=csv_player.birth_date,
            college=csv_player.college_name,
        )

        return db_player

    def _parse_csv_height(self, csv_height: str) -> int:
        split_height: List[str] = csv_height.split("-")

        error_message: str = f'Invalid height format "{csv_height}"'
        if len(split_height) != 2:
            raise ValueError(error_message)

        try:
            feet: int = int(split_height[0])
            inches: int = int(split_height[1])
        except ValueError:
            raise ValueError(error_message)

        return feet * 12 + inches
