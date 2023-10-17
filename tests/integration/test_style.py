from typing import Optional
import datetime


def bad_import_order(num_days: Optional[int]):
    date = datetime.date(2020, 3, 9)
    if num_days is not None:
        date += datetime.timedelta(days=num_days)

    return date
