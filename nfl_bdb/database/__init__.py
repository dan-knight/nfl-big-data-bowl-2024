from os import getenv
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import create_engine

from nfl_bdb.database.models import Base
from nfl_bdb.database.models.game import Game  # pyright: ignore[reportUnusedImport]
from nfl_bdb.database.models.play import Play  # pyright: ignore[reportUnusedImport]
from nfl_bdb.database.models.player import Player  # pyright: ignore[reportUnusedImport]
from nfl_bdb.database.models.tackle import Tackle  # pyright: ignore[reportUnusedImport]
from nfl_bdb.database.models.team import Team  # pyright: ignore[reportUnusedImport]
from nfl_bdb.database.models.tracking import (
    TrackingPoint,  # pyright: ignore[reportUnusedImport]
)


def set_up_engine():
    engine = create_engine(get_db_uri())
    return engine


def get_db_uri() -> str:
    load_dotenv()

    DB_URI_ENVVAR: str = "DATABASE_URI"
    database_uri: Optional[str] = getenv(DB_URI_ENVVAR)
    if database_uri is None:
        raise EnvironmentError(f'No environment variable "{DB_URI_ENVVAR}" found.')

    return database_uri


engine = set_up_engine()


def build_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
