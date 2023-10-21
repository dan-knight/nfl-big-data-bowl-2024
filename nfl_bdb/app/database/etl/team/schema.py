from dataclasses import dataclass


@dataclass(frozen=True)
class CSVTeam:
    abbreviation: str
