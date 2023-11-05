import datetime
from typing import Dict, Optional, List

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
        return {
            team.abbreviation: team for team in db_teams
        }
