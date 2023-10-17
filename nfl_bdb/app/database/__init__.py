from os import getenv
from typing import Optional
from dotenv import load_dotenv
from sqlalchemy import create_engine

from nfl_bdb.app.database.models import Base  # pyright: ignore[reportUnusedImport]


def set_up_engine():
    load_dotenv()

    DB_URI_ENVVAR: str = "DATABASE_URI"
    database_uri: Optional[str] = getenv(DB_URI_ENVVAR)
    if database_uri is None:
        raise EnvironmentError(f"No environment variable \"{DB_URI_ENVVAR}\" found.")

    engine = create_engine(database_uri)
    return engine


engine = set_up_engine()


def build_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

