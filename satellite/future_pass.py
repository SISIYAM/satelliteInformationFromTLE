from datetime import timedelta
from skyfield.api import Topos
from satellite.time import CurrentTime

class FuturePass:
    def __init__(self, timescale, observer_location):
        self.ts = timescale
        self.observer_location = observer_location

    def calculate(self, satellite, duration_days=1):
        observer = Topos(latitude_degrees=self.observer_location['latitude'],
                         longitude_degrees=self.observer_location['longitude'])
        t0 = self.ts.utc(CurrentTime().get_utc())
        t1 = self.ts.utc(CurrentTime().get_utc() + timedelta(days=duration_days))
        times, events = satellite.find_events(observer, t0, t1)
        if len(times) < 3:
            raise ValueError("Not enough events found for a complete pass.")
        pass_times = {
            'Rise': times[0].utc_datetime(),
            'Culminate': times[1].utc_datetime(),
            'Set': times[2].utc_datetime()
        }
        return pass_times
