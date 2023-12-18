from nfl_bdb.database.etl.team.schema import CSVTeam
from nfl_bdb.database.models.team import Team as DBTeam


class TeamFactory:
    def transform_team(self, csv_team: CSVTeam) -> DBTeam:
        return DBTeam(abbreviation=csv_team.abbreviation)
