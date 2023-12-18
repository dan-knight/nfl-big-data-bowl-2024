import datetime
from typing import List

from nfl_bdb.database.etl.factory import ETLFactory, FactoryTeamIndex
from nfl_bdb.database.etl.game.schema import CSVGame
from nfl_bdb.database.models.game import Game as DBGame
from nfl_bdb.database.models.team import Team as DBTeam


class GameFactory(ETLFactory, FactoryTeamIndex):
    def __init__(self, db_teams: List[DBTeam]):
        super().__init__(db_teams=db_teams)

    def transform_game(self, csv_game: CSVGame) -> DBGame:
        home_team: DBTeam = self._get_team(csv_game.home_team)
        away_team: DBTeam = self._get_team(csv_game.away_team)
        kickoff_time: datetime.datetime = datetime.datetime.combine(
            csv_game.game_date, csv_game.game_time
        )

        return DBGame(
            game_id=csv_game.game_id,
            kickoff_time=kickoff_time,
            home_team=home_team,
            away_team=away_team,
            home_score=csv_game.home_score,
            away_score=csv_game.away_score,
        )
