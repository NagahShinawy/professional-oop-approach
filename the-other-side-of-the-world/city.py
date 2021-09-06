"""
created by Nagaj at 11/06/2021
"""

EMPTY = "city can not be empty"
INVALID_CITY_NAME = "Invalid City Name"


def validate_city(function):
    def wrapper(*args, **kwargs):
        city = function(*args, **kwargs)
        if city == "":
            raise ValueError(EMPTY)
        if len(city) < 3:
            raise ValueError(INVALID_CITY_NAME)
        return city

    return wrapper


@validate_city
def user_city_name():
    return input("Enter Your City")


def city_location_by_name(city):
    pass
