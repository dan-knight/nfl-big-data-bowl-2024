from nfl_bdb.app.database.etl.team.schema import CSVTeam
from nfl_bdb.app.database.models.team import Team as DBTeam


class TeamFactory:
    def transform_team(self, csv_team: CSVTeam) -> DBTeam:
        return DBTeam(abbreviation=csv_team.abbreviation)
