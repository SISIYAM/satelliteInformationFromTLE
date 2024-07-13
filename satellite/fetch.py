import requests
import time
from tqdm import tqdm
from skyfield.api import EarthSatellite

class FetchTelemetryData:
    def __init__(self, timescale):
        self.ts = timescale

    def fetch(self, sat):
        url = f'https://celestrak.org/NORAD/elements/gp.php?NAME={sat}&FORMAT=tle'
        with tqdm(total=1, desc="Please wait fetching TLE data..", leave=False) as pbar:
            response = requests.get(url)
            time.sleep(2)  # Simulate a delay for fetching data
            pbar.update(1)
        if response.ok:
            data = response.text.strip().splitlines()
            satName = data[0]
            lineOne = data[1]
            lineTwo = data[2]
            return EarthSatellite(lineOne, lineTwo, satName, self.ts)
        else:
            return "Failed while fetching data"
