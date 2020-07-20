from datetime import datetime as _datetime
from datetime import timedelta as _timedelta

_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"
_TIMESTAMP_FORMAT_2 = "%Y-%m-%dT%H:%M:%S%z"
_TIME_KEYS = ['day', 'hour', 'minute', 'second', 'microsecond']

def parse_timestamp_utc(timestamp):
    if timestamp:
        try:
            return _datetime.strptime(timestamp, _TIMESTAMP_FORMAT)
        except ValueError:
            return _datetime.strptime(timestamp, _TIMESTAMP_FORMAT_2)
    else:
        return None

def parse_timestamp_local(timestamp):
    if timestamp:
        return parse_timestamp_utc(timestamp).astimezone()
    else:
        return None

def _generate_trim_function(index):
    def func(timestamp):
        for key in _TIME_KEYS[index+1:]:
            timestamp -= _timedelta(**{
                f'{key}s': getattr(timestamp, key)
            })
        return timestamp
    return func

for idx, key in enumerate(_TIME_KEYS[:-1]):
    globals()[f'trim_{key}'] = _generate_trim_function(idx)