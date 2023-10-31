import datetime
from typing import Dict, Any
import unittest
from nfl_bdb.app.database.etl.fields import DATETIME_FORMAT
from nfl_bdb.app.database.etl.tracking.schema import CSVTracking, CSVTrackingSchema


class TestCSVTrackingSchema(unittest.TestCase):
    def _create_csv_tracking_dict(self, csv_tracking: CSVTracking) -> Dict[str, Any]:
        player_id: int | str = csv_tracking.player_id if csv_tracking.player_id is not None else "NA"
        tracking_time: str = csv_tracking.time.strftime(DATETIME_FORMAT)
        jersey_number: str = csv_tracking.jersey_number if csv_tracking.jersey_number is not None else "NA"
        orientation: float | str = csv_tracking.orientation if csv_tracking.orientation is not None else "NA"
        direction: float | str = csv_tracking.direction if csv_tracking.direction is not None else "NA"
        event: float | str = csv_tracking.event if csv_tracking.event is not None else "NA"

        result: Dict[str, Any] = {
            "gameId": csv_tracking.game_id,
            "playId": csv_tracking.play_id,
            "nflId": player_id,
            "displayName": csv_tracking.player_name,
            "frameId": csv_tracking.frame,
            "time": tracking_time,
            "jerseyNumber": jersey_number,
            "club": csv_tracking.team,
            "playDirection": csv_tracking.play_direction,
            "x": csv_tracking.x,
            "y": csv_tracking.y,
            "s": csv_tracking.speed,
            "a": csv_tracking.acceleration,
            "dis": csv_tracking.distance,
            "o": orientation,
            "dir": direction,
            "event": event
        }

        return result

    def test__tracking_schema__handles_valid_values(self):
        tracking = CSVTracking(
            game_id=89,
            play_id=1728,
            player_id=120,
            player_name="Josh Allen",
            frame=888,
            time=datetime.datetime(2022, 10, 11, 1, 15, 32, 140000),
            jersey_number="12",
            team="BUF",
            play_direction="left",
            x=-1.02,
            y=3.21,
            speed=12.3,
            acceleration=0.03,
            distance=0.09,
            orientation=230.1,
            direction=141.6,
            event="tackle"
        )

        tracking_dict: Dict[str, Any] = self._create_csv_tracking_dict(tracking)

        schema = CSVTrackingSchema()
        result = schema.load(tracking_dict)

        assert result == tracking
    
    def test__tracking_schema__handles_na_player_id(self):
        tracking = CSVTracking(
            game_id=89,
            play_id=1728,
            player_id=None,
            player_name="Josh Allen",
            frame=888,
            time=datetime.datetime(2022, 10, 11, 1, 15, 32, 140000),
            jersey_number="12",
            team="BUF",
            play_direction="left",
            x=-1.02,
            y=3.21,
            speed=12.3,
            acceleration=0.03,
            distance=0.09,
            orientation=230.1,
            direction=141.6,
            event="tackle"
        )

        tracking_dict: Dict[str, Any] = self._create_csv_tracking_dict(tracking)

        schema = CSVTrackingSchema()
        result = schema.load(tracking_dict)

        assert result == tracking
    
    def test__tracking_schema__handles_na_jersey_number(self):
        tracking = CSVTracking(
            game_id=89,
            play_id=1728,
            player_id=123,
            player_name="Josh Allen",
            frame=888,
            time=datetime.datetime(2022, 10, 11, 1, 15, 32, 140000),
            jersey_number=None,
            team="BUF",
            play_direction="left",
            x=-1.02,
            y=3.21,
            speed=12.3,
            acceleration=0.03,
            distance=0.09,
            orientation=230.1,
            direction=141.6,
            event="tackle"
        )

        tracking_dict: Dict[str, Any] = self._create_csv_tracking_dict(tracking)

        schema = CSVTrackingSchema()
        result = schema.load(tracking_dict)

        assert result == tracking
    
    def test__tracking_schema__handles_na_orientation(self):
        tracking = CSVTracking(
            game_id=89,
            play_id=1728,
            player_id=123,
            player_name="Josh Allen",
            frame=888,
            time=datetime.datetime(2022, 10, 11, 1, 15, 32, 140000),
            jersey_number="12",
            team="BUF",
            play_direction="left",
            x=-1.02,
            y=3.21,
            speed=12.3,
            acceleration=0.03,
            distance=0.09,
            orientation=None,
            direction=141.6,
            event="tackle"
        )

        tracking_dict: Dict[str, Any] = self._create_csv_tracking_dict(tracking)

        schema = CSVTrackingSchema()
        result = schema.load(tracking_dict)

        assert result == tracking
    
    def test__tracking_schema__handles_na_direction(self):
        tracking = CSVTracking(
            game_id=89,
            play_id=1728,
            player_id=123,
            player_name="Josh Allen",
            frame=888,
            time=datetime.datetime(2022, 10, 11, 1, 15, 32, 140000),
            jersey_number="12",
            team="BUF",
            play_direction="left",
            x=-1.02,
            y=3.21,
            speed=12.3,
            acceleration=0.03,
            distance=0.09,
            orientation=230.1,
            direction=None,
            event="tackle"
        )

        tracking_dict: Dict[str, Any] = self._create_csv_tracking_dict(tracking)

        schema = CSVTrackingSchema()
        result = schema.load(tracking_dict)

        assert result == tracking
    
    def test__tracking_schema__handles_na_event(self):
        tracking = CSVTracking(
            game_id=89,
            play_id=1728,
            player_id=123,
            player_name="Josh Allen",
            frame=888,
            time=datetime.datetime(2022, 10, 11, 1, 15, 32, 140000),
            jersey_number="12",
            team="BUF",
            play_direction="left",
            x=-1.02,
            y=3.21,
            speed=12.3,
            acceleration=0.03,
            distance=0.09,
            orientation=230.1,
            direction=141.6,
            event=None
        )

        tracking_dict: Dict[str, Any] = self._create_csv_tracking_dict(tracking)

        schema = CSVTrackingSchema()
        result = schema.load(tracking_dict)

        assert result == tracking