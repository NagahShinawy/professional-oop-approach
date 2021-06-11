"""
created by Nagaj at 11/06/2021
"""

MADRID_LAT = float("40.4168")  # process of abstraction
MADRID_LONG = float("-3.7038")  # # process of abstraction


anti_lat = MADRID_LAT.__add__(float("-180"))
print(anti_lat)
anti_lat = anti_lat.__add__(float("180"))
print(anti_lat)
