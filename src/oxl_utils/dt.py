from os import environ
from datetime import datetime

from pytz import timezone


def datetime_w_tz(tz: (timezone, str) = None) -> datetime:
    if tz in [None, '']:
        try:
            tz = environ['TIMEZONE']

        except KeyError:
            raise EnvironmentError('TIMEZONE not provided')

    if isinstance(tz, str):
        tz = timezone(tz)

    return datetime.now(tz)
