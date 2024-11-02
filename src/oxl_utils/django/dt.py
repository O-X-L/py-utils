from datetime import datetime

from pytz import utc
from


def datetime_from_db(dt: (datetime, None), timezone: str) -> (datetime, None):
    # datetime form db will always be UTC; convert it
    if not isinstance(dt, datetime):
        return None

    local_dt = dt.replace(tzinfo=utc).astimezone(TIMEZONE)
    return TIMEZONE.normalize(local_dt)
