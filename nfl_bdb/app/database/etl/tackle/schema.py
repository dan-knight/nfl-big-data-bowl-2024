from dataclasses import dataclass


@dataclass(frozen=True)
class CSVTackle:
    game_id: int
    play_id: int
    player_id: int
    tackle: bool
    assist: bool
    forced_fumble: bool
    pff_missed_tackle: bool
