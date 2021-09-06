"""
created by Nagaj at 11/06/2021
"""


class Location:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"Lat<{self.lat}>, Lon<{self.lon}>"

    def is_valid(self):
        pass
