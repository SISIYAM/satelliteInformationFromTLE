import math

class Angle:
    def __init__(self, satellite_longitude, site_longitude, site_latitude):
        self.satellite_longitude = satellite_longitude
        self.site_longitude = site_longitude
        self.site_latitude = site_latitude

    def calculate_elevation_azimuth(self):
        S_rad = math.radians(self.satellite_longitude)
        N_rad = math.radians(self.site_longitude)
        L_rad = math.radians(self.site_latitude)
        
        G = S_rad - N_rad
        
        numerator = math.cos(G) * math.cos(L_rad) - 0.1512
        denominator = math.sqrt(1 - (math.cos(G) * math.cos(L_rad))**2)
        E = math.atan(numerator / denominator)
        
        E_deg = math.degrees(E)
        
        tan_G = math.tan(G)
        sin_L = math.sin(L_rad)
        A = math.atan(tan_G / sin_L)
        
        A_deg = math.degrees(A)
        
        return E_deg, A_deg
