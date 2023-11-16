import csv
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

from nfl_bdb.app.database.etl.game import GameFactory
from nfl_bdb.app.database.etl.game.schema import CSVGame, CSVGameSchema
from nfl_bdb.app.database.etl.play import PlayFactory
from nfl_bdb.app.database.etl.play.schema import CSVPlay, CSVPlaySchema
from nfl_bdb.app.database.etl.player import PlayerFactory
from nfl_bdb.app.database.etl.player.schema import CSVPlayer, CSVPlayerSchema
from nfl_bdb.app.database.etl.tackle import TackleFactory
from nfl_bdb.app.database.etl.tackle.schema import CSVTackle, CSVTackleSchema
from nfl_bdb.app.database.etl.team import TeamFactory
from nfl_bdb.app.database.etl.team.schema import CSVTeam
from nfl_bdb.app.database.etl.tracking import TrackingFactory, get_tracking_files
from nfl_bdb.app.database.etl.tracking.schema import CSVTracking, CSVTrackingSchema
from nfl_bdb.app.database.models import Base
from nfl_bdb.app.database.models.game import Game as DBGame
from nfl_bdb.app.database.models.play import Play as DBPlay
from nfl_bdb.app.database.models.player import Player as DBPlayer
from nfl_bdb.app.database.models.tackle import Tackle as DBTackle
from nfl_bdb.app.database.models.team import Team as DBTeam
from nfl_bdb.app.database.models.tracking import TrackingPoint as DBTracking

RawCSV = Dict[str, str]


def load_csv(path: Path) -> Iterable[RawCSV]:
    csv_file = open(path)
    reader = csv.DictReader(csv_file)

    return reader


def import_nfl_data(data_directory_path: Path) -> List[Base]:
    players: List[DBPlayer] = import_players(data_directory_path / "players.csv")

    games: List[DBGame]
    teams: List[DBTeam]
    games, teams = import_games_and_teams(data_directory_path / "games.csv")

    plays: List[DBPlay] = import_plays(data_directory_path / "plays.csv", teams)
    tackles: List[DBTackle] = import_tackles(data_directory_path / "tackles.csv", plays)

    tracking_data_paths: List[Path] = get_tracking_files(data_directory_path)
    tracking: List[DBTracking] = import_all_tracking(tracking_data_paths, plays)

    return [*players, *games, *teams, *plays, *tackles, *tracking]


def import_players(player_data_path: Path) -> List[DBPlayer]:
    raw_players: Iterable[RawCSV] = load_csv(player_data_path)

    schema = CSVPlayerSchema()
    factory = PlayerFactory()

    def transform(raw_player: RawCSV) -> DBPlayer:
        csv_player: CSVPlayer = schema.load(raw_player)
        return factory.transform_player(csv_player)

    db_players: List[DBPlayer] = [transform(player) for player in raw_players]

    return db_players


def import_games_and_teams(game_data_path: Path) -> Tuple[List[DBGame], List[DBTeam]]:
    raw_games: Iterable[RawCSV] = load_csv(game_data_path)

    game_schema = CSVGameSchema()

    csv_games: List[CSVGame] = [game_schema.load(game) for game in raw_games]

    def extract_team_names(games: List[CSVGame]) -> Set[str]:
        team_names: List[str] = [
            *[csv_game.home_team for csv_game in csv_games],
            *[csv_game.away_team for csv_game in csv_games],
        ]

        return set(team_names)

    csv_teams: List[CSVTeam] = [
        CSVTeam(abbreviation=team_name) for team_name in extract_team_names(csv_games)
    ]

    team_factory = TeamFactory()
    db_teams: List[DBTeam] = [
        team_factory.transform_team(csv_team) for csv_team in csv_teams
    ]

    game_factory = GameFactory(db_teams)
    db_games: List[DBGame] = [
        game_factory.transform_game(csv_game) for csv_game in csv_games
    ]

    return db_games, db_teams


def import_plays(play_data_path: Path, db_teams: List[DBTeam]) -> List[DBPlay]:
    raw_plays: Iterable[RawCSV] = load_csv(play_data_path)

    play_schema = CSVPlaySchema()
    csv_plays: List[CSVPlay] = [play_schema.load(raw_play) for raw_play in raw_plays]

    play_factory = PlayFactory(db_teams)
    db_plays: List[DBPlay] = [
        play_factory.transform_play(csv_play) for csv_play in csv_plays
    ]

    return db_plays


def import_tracking(
    tracking_data_path: Path, db_plays: List[DBPlay]
) -> List[DBTracking]:
    raw_tracking: Iterable[RawCSV] = load_csv(tracking_data_path)

    tracking_schema = CSVTrackingSchema()
    csv_tracking: List[CSVTracking] = [
        tracking_schema.load(raw_tracking_point) for raw_tracking_point in raw_tracking
    ]

    tracking_factory = TrackingFactory(db_plays)
    db_tracking: List[DBTracking] = [
        tracking_factory.transform_tracking(csv_tracking_point)
        for csv_tracking_point in csv_tracking
    ]

    return db_tracking


def import_all_tracking(
    tracking_data_paths: List[Path], db_plays: List[DBPlay]
) -> List[DBTracking]:
    return [
        tracking
        for result in (import_tracking(path, db_plays) for path in tracking_data_paths)
        for tracking in result
    ]


def import_tackles(tackle_data_path: Path, db_plays: List[DBPlay]) -> List[DBTackle]:
    raw_tackles: Iterable[RawCSV] = load_csv(tackle_data_path)

    schema = CSVTackleSchema()
    csv_tackles: List[CSVTackle] = [
        schema.load(raw_tackle) for raw_tackle in raw_tackles
    ]

    tackle_factory = TackleFactory(db_plays)
    db_tackles: List[DBTackle] = [
        tackle_factory.transform_tackle(csv_tackle) for csv_tackle in csv_tackles
    ]

    return db_tackles
