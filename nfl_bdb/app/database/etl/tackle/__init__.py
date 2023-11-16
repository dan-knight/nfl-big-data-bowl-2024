from nfl_bdb.app.database.etl.factory import ETLFactory, FactoryPlayIndex
from nfl_bdb.app.database.etl.tackle.schema import CSVTackle
from nfl_bdb.app.database.models.play import Play as DBPlay
from nfl_bdb.app.database.models.tackle import Tackle as DBTackle


class TackleFactory(ETLFactory, FactoryPlayIndex):
    def transform_tackle(self, csv_tackle: CSVTackle) -> DBTackle:
        play: DBPlay = self._get_play(csv_tackle.game_id, csv_tackle.play_id)

        return DBTackle(
            play=play,
            player_id=csv_tackle.player_id,
            tackled=csv_tackle.tackle,
            assist=csv_tackle.assist,
            forced_fumble=csv_tackle.assist,
            missed=csv_tackle.pff_missed_tackle,
        )
