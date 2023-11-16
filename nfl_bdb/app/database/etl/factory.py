import datetime
from collections import defaultdict
from typing import Dict, List, Optional

from nfl_bdb.app.database.models.play import Play as DBPlay
from nfl_bdb.app.database.models.team import Team as DBTeam


class ETLFactory:
    def _parse_csv_date(self, csv_date: str) -> datetime.date:
        ...

    def _parse_csv_datetime(self, csv_datetime: str) -> datetime.datetime:
        ...

    @property
    def _csv_date_format(self) -> str:
        ...

    @property
    def _csv_datetime_format(self) -> str:
        ...


class FactoryTeamIndex:
    def __init__(self, db_teams: List[DBTeam]):
        self._db_team_index: Dict[str, DBTeam] = self._index_teams(db_teams)

    def _get_team(self, abbreviation: str) -> DBTeam:
        team: Optional[DBTeam] = self._db_team_index.get(abbreviation)

        if team is None:
            raise LookupError(f"No team found with abbreviation {abbreviation}.")

        return team

    def _index_teams(self, db_teams: List[DBTeam]) -> Dict[str, DBTeam]:
        return {team.abbreviation: team for team in db_teams}


class FactoryPlayIndex:
    def __init__(self, db_plays: List[DBPlay]):
        self._play_index: Dict[int, Dict[int, DBPlay]] = self._index_plays(db_plays)

    def _index_plays(self, db_plays: List[DBPlay]) -> Dict[int, Dict[int, DBPlay]]:
        play_index: Dict[int, Dict[int, DBPlay]] = defaultdict(lambda: {})

        for play in db_plays:
            game_index: Dict[int, DBPlay] = play_index[play.game_id]
            game_index[play.ingame_play_id] = play

        return play_index

    def _get_play(self, game_id: int, ingame_play_id: int) -> DBPlay:
        try:
            return self._play_index[game_id][ingame_play_id]
        except IndexError:
            raise ValueError(f"No play {ingame_play_id} found from game {game_id}")
