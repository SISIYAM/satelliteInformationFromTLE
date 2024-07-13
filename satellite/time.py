import pytz
from datetime import datetime
from skyfield.api import utc

class CurrentTime:
    def __init__(self):
        self.dhaka_time_zone = pytz.timezone('Asia/Dhaka')
    
    def get_utc(self):
        return datetime.utcnow().replace(tzinfo=utc)
    
    def get_dhaka_time(self):
        utc_time = self.get_utc()
        return utc_time.astimezone(self.dhaka_time_zone)
    
    def pretty_print_passing_time(self, passing_time):
        formatted_output = "Future Pass Times of Satellite Relative to Observer (Ground Station):\n"
        for event, time in passing_time.items():
            dhaka_time = time.astimezone(self.dhaka_time_zone)
            formatted_output += f"\n\t{event}: {dhaka_time.strftime('%d %b %Y %I:%M:%S %p UTC')} \n"
        return formatted_output
