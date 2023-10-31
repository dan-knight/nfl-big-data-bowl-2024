import csv
from pathlib import Path
from typing import Dict, Iterable, List

from nfl_bdb.app.database.models import Base


def load_csv(path: Path) -> Iterable[Dict[str, str]]:
    csv_file = open(path)
    reader = csv.DictReader(csv_file)

    return reader


def import_nfl_data(data_path: Path) -> List[Base]:
    ...
