from datetime import datetime as _datetime
from datetime import timedelta as _timedelta

_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"

def parse_timestamp_utc(timestamp):
    if timestamp:
        return _datetime.strptime(timestamp, _TIMESTAMP_FORMAT)
    else:
        return None

def parse_timestamp_local(timestamp):
    if timestamp:
        return parse_timestamp_utc(timestamp).astimezone()
    else:
        return None