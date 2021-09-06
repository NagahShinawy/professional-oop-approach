"""
created by Nagaj at 11/06/2021
"""
import os
import folium
from location import Location


MAPS = "./data/maps/"
MALKA_PATH = os.path.join(MAPS, "malka.html")
OPEN = "start {path}"
MACHINES = {"mac": "Darwin", "windows": "Windows", "linux": "Linux"}
MALKA = {"lat": 24.799940, "lon": 46.597690}


def main():
    malka_location = Location(lat=MALKA["lat"], lon=MALKA["lon"])
    malka_map = folium.Map(
        location=[malka_location.lat, malka_location.lon],
        width="%50",
        height="%50",
        left="%25",
        top="%25"
    )
    malka_map.save(MALKA_PATH)
    os.system(OPEN.format(path=os.path.abspath(MALKA_PATH)))


if __name__ == "__main__":
    main()
