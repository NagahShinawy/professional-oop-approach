"""
created by Nagaj at 11/06/2021
"""
# actually we don't use NUMBER(abstract base layer or template to others to follow) i use FLOAT, INT, LONG
MADRID_LAT = float("40.4168")  # process of abstraction
MADRID_LONG = float("-3.7038")  # # process of abstraction

print(f"Madrid lat: {MADRID_LAT}")
print(f"Madrid lon: {MADRID_LONG}")

print("#" * 50)

ANTIPOD_LAT = MADRID_LAT * -1
ANTIPOD_LON = MADRID_LONG * -1

print(f"Anti Madrid lat: {ANTIPOD_LAT}")
print(f"Anti Madrid lon: {ANTIPOD_LON}")


print(ANTIPOD_LAT.__mul__(int("-10")))
