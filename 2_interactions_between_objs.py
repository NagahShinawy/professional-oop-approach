"""
created by Nagaj at 11/06/2021
"""

MADRID_LAT = float("40.4168")  # process of abstraction
MADRID_LONG = float("-3.7038")  # # process of abstraction

ANTIPOD_LAT = MADRID_LAT * -1  # 1
ANTIPOD_LON = MADRID_LONG * -1  # 2

print(f"Anti Madrid lat: {ANTIPOD_LAT}")
print(f"Anti Madrid lon: {ANTIPOD_LON}")

anti_lat = MADRID_LAT.__mul__(-1)  # 1
anti_lon = MADRID_LONG.__mul__(-1)  # 2

print(anti_lat)
print(anti_lon)