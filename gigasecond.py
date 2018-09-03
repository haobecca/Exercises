from datetime import datetime, date, time
from datetime import timedelta

def add_gigasecond(birth_date):
    d = birth_date
    if d.hour == 0:
        t = time(0, 0, 0)
        return datetime.combine(d, t) + timedelta(seconds = 1000000000)
    else:
        return birth_date + timedelta(seconds = 1000000000)

