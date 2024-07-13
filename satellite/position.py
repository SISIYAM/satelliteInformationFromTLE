from datetime import datetime
from skyfield.api import wgs84

class SatellitePosition:
    def __init__(self, earth_satellite, timescale):
        self.satellite = earth_satellite
        self.ts = timescale

    def propagate(self):
        # Get the current time
        now = datetime.utcnow()

        # Convert current time to a Skyfield Time object
        t = self.ts.utc(now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Compute the satellite's position
        geocentric = self.satellite.at(t)

        # Get the geodetic position (latitude, longitude)
        subpoint = wgs84.subpoint(geocentric)
        latitude = subpoint.latitude.degrees
        longitude = subpoint.longitude.degrees

        return latitude, longitude
