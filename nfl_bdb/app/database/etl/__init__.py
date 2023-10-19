import csv
from pathlib import Path
from typing import Dict, Iterable


def load_csv(path: Path) -> Iterable[Dict[str, str]]:
    csv_file = open(path)
    reader = csv.DictReader(csv_file)

    return reader

