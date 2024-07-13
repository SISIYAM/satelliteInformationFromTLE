from skyfield.api import load
from satellite.fetch import FetchTelemetryData
from satellite.future_pass import FuturePass
from satellite.position import SatellitePosition
from satellite.angle import Angle
from satellite.time import CurrentTime

class SatelliteTracker:
    def __init__(self, observer_location):
        self.observer_location = observer_location
        self.ts = load.timescale()
        self.telemetry_data_fetcher = FetchTelemetryData(self.ts)
        self.future_pass_calculator = FuturePass(self.ts, self.observer_location)
        self.currentTime = CurrentTime()

    def fetch_telemetry_data(self, sat):
        return self.telemetry_data_fetcher.fetch(sat)

    def get_local_time(self):
        return self.currentTime.get_dhaka_time()

    def get_passing_time(self, satellite):
        return self.future_pass_calculator.calculate(satellite)

    def get_satellite_position(self, satellite):
        sat_position = SatellitePosition(satellite, self.ts)
        return sat_position.propagate()

    def get_elevation_azimuth(self, satellite):
        latitude, longitude = self.get_satellite_position(satellite)
        angle_calculator = Angle(longitude, self.observer_location['longitude'], self.observer_location['latitude'])
        return angle_calculator.calculate_elevation_azimuth()
