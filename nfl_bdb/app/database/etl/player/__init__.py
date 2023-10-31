import datetime
from typing import Optional
from nfl_bdb.app.database.etl.factory import ETLFactory
from nfl_bdb.app.database.etl.player.schema import CSVPlayer
from nfl_bdb.app.database.models.player import Player as DBPlayer


class PlayerFactory(ETLFactory):
    def transform_player(self, csv_player: CSVPlayer) -> DBPlayer:
        height: int = self._parse_csv_height(csv_player.height)

        birth_date: Optional[datetime.date] = (
            self._parse_csv_date(csv_player.birth_date)
            if csv_player.birth_date is not None
            else None
        )

        db_player = DBPlayer(
            player_id=csv_player.player_id,
            name=csv_player.name,
            position=csv_player.position,
            height=height,
            weight=csv_player.weight,
            birth_date=birth_date,
            college=csv_player.college_name,
        )

        return db_player

    def _parse_csv_height(self, csv_height: str) -> int:
        ...
