from datetime import datetime, time, timedelta, date

class Today:
    def get_start_day_timestamp(self: object) -> int:
        return int(round(datetime.combine(datetime.now(), time.min).timestamp()))

    def get_end_day_timestamp(self: object) -> int:
        return int(round(datetime.combine(datetime.now(), time.max).timestamp())) 

class Tomorrow:
    def get_tomorrow_start(self: object):
        return int(round(datetime.combine((date.today() + timedelta(days=1)), time.min).timestamp()))
    
    def get_tomorrow_end(self: object):
        return int(round(datetime.combine((date.today() + timedelta(days=1)), time.max).timestamp()))
