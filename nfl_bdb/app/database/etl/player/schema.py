from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CSVPlayer:
    nfl_id: int
    height: str
    weight: int
    birth_date: Optional[str]
    display_name: str
    position: str
    college_name: str
