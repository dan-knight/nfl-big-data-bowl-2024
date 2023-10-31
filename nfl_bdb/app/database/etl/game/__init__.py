import datetime
from typing import Dict
from nfl_bdb.app.database.etl.factory import ETLFactory, FactoryTeamIndex
from nfl_bdb.app.database.etl.game.schema import CSVGame
from nfl_bdb.app.database.models.game import Game as DBGame
from nfl_bdb.app.database.models.team import Team as DBTeam


class GameFactory(ETLFactory, FactoryTeamIndex):
    def __init__(self, db_team_index: Dict[str, DBTeam]):
        self.db_team_index: Dict[str, DBTeam] = db_team_index

    def transform_game(self, csv_game: CSVGame) -> DBGame:
        home_team: DBTeam = self._get_team(csv_game.home_team)
        away_team: DBTeam = self._get_team(csv_game.away_team)
        kickoff_time: datetime.date = self._parse_csv_datetime(csv_game.game_date)

        return DBGame(
            game_id=csv_game.game_id,
            kickoff_time=kickoff_time,
            home_team=home_team,
            away_team=away_team,
            home_score=csv_game.home_score,
            away_score=csv_game.away_score,
        )
