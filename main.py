from satellite.tracker import SatelliteTracker
from satellite.time import CurrentTime

# Define observer location (latitude and longitude in degrees)
observer_location = {
    'latitude': 24.293482,
    'longitude': 89.081394
}

# Create SatelliteTracker object
tracker = SatelliteTracker(observer_location)

# Create currentTime Object
current_time = CurrentTime()

# Fetch telemetry data for a satellite
satelliteName = input("\nEnter the name of the CUBESAT (e.g. CUTE-1 (CO-55)): ")
satellite = tracker.fetch_telemetry_data(satelliteName)

print(f"\n\n\t\t Satellite: {satelliteName} \t\t\n\n")
# Get current local time
local_time = tracker.get_local_time().strftime('%d %b %Y %I:%M:%S %p UTC')
print(f"\nLocal Time:  \n\n \t{local_time}\n")

print(f"Observer position: \n")
print(f"\t Latitude: {observer_location['latitude']}\n")
print(f"\t Longitude: {observer_location['longitude']}\n")

# Get future passing time
passing_time = tracker.get_passing_time(satellite)
formatted_passing_time = current_time.pretty_print_passing_time(passing_time)
print(formatted_passing_time)

# Get satellite position
latitude, longitude = tracker.get_satellite_position(satellite)
print(f"Satellite Position :\n\n\tLatitude: {latitude:.2f} \n\n\tLongitude: {longitude:.2f} \n")

# Calculate elevation and azimuth
elevation, azimuth = tracker.get_elevation_azimuth(satellite)
print(f"Elevation angle: {elevation:.2f} degrees \n")
print(f"Azimuth angle: {azimuth:.2f} degrees \n")
