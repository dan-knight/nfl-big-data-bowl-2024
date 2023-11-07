from typing import Dict, Optional
from nfl_bdb.app.database.etl.factory import ETLFactory, FactoryPlayIndex
from nfl_bdb.app.database.etl.tracking.schema import CSVTracking
from nfl_bdb.app.database.models.tracking import TrackingPoint as DBTracking


class TrackingFactory(ETLFactory, FactoryPlayIndex):
    def transform_tracking(self, csv_tracking: CSVTracking) -> DBTracking:
        play_id: int = self._get_play(csv_tracking.game_id, csv_tracking.play_id).play_id
        direction: bool = self._parse_play_direction(csv_tracking.play_direction)

        return DBTracking(
            play_id=play_id,
            player_id=csv_tracking.player_id,
            frame=csv_tracking.frame,
            timestamp=csv_tracking.time,
            x=csv_tracking.x,
            y=csv_tracking.y,
            speed=csv_tracking.speed,
            acceleration=csv_tracking.acceleration,
            direction=direction,
            orientation=csv_tracking.orientation,
            distance_traveled=csv_tracking.distance,
            jersey=csv_tracking.jersey_number,
            event=csv_tracking.event,
        )

    def _parse_play_direction(self, csv_direction: str) -> bool:
        direction_index: Dict[str, bool] = {"right": True, "left": False}

        play_direction: Optional[bool] = direction_index.get(csv_direction)

        if play_direction is None:
            raise ValueError(f'Invalid play direction "{csv_direction}"')

        return play_direction
