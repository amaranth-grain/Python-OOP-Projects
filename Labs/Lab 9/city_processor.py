"""
This module contains the data structures and code to query the
Open Notify API and process the times that the ISS will be directly
overhead a city.
"""
import requests
import pandas
import json
import datetime


def jprint(obj):
    """
    Create and print a formatted string of the Python JSON object
    """
    #
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


class City:
    """
    Represents the location of a city. An object of this class consists
    of 3 parameters:
    - city: the name of the city (a string)
    - lat: the latitude of the city (a float)
    - lng: the longitude of the city (a float)

    """

    def __init__(self, city_ascii: str, lat: float, lng: float):
        """
        Initialized a CityLocation object with the provided city name,
        latitude and longitude
        :param city_ascii: a string
        :param lat: a float in the range [0,90]
        :param lng: a float in the range [0,180]
        """
        self.city_name = city_ascii
        if not -90 <= lat <= 90:
            print(lat)
            raise ValueError("latitude needs to be in range[0,90]")
        if not -190 <= lng <= 180:
            raise ValueError("Longitude needs to be in range [0,180]")
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return f"City: {self.city_name}, Lat: {self.lat}, Lng: {self.lng}"


class CityDatabase:
    """
    Represents a list of cities and their locations.
    """

    def __init__(self, file_path):
        """
        Initializes a CityDatabase object by reading an excel file of
        city information using pandas, converting the data into a City
        object and storing it in a list.
        :param file_path: the file path to an excel file.
        :precondition file_path: the excel file at the specified path should
        have 3 columns with the headers "city_ascii", "lat", and "lng"
        """
        # will raise an error if the path is invalid, we don't need an
        # if statement here
        df = pandas.read_excel(file_path)

        """
        read in the cities using a dictionary comprehension
        dictionary = { key: value for elem in iterable }
        In this case we are reading in the name of the city as the key 
        and its corresponding CityLocation object as the value. We 
        have made the assumption that each city ahs a unique name.
        """
        #
        self.city_db = [
            City(row[1]["city_ascii"], row[1]["lat"], row[1]["lng"])
            for row in df.iterrows()]

    def __str__(self):
        output = ""
        for city in self.city_db:
            output += f"City: {city.city_name}\nLat: {city.lat} Lng: " \
                   f"{city.lng}\n\n"
        return output


class OverheadPassEvent:
    """
    Represents a time that the ISS station will be directly overhead a
    location. The attributes are:
    - duration:
    The time in seconds that the ISS will be directly overhead
    - risetime:
    a DateTime object specifying the time and date it will be overhead
    """

    def __init__(self, duration, risetime):
        self.duration = duration
        self.risetime = datetime.datetime.fromtimestamp(risetime)

    def __str__(self):
        return f"{self.risetime} for {self.duration} seconds"


class CityOverheadTimes:
    """
    A data structure to store a city and the associated times that the
    ISS station will be directly overhead it. It's attributes are:
    - city: a City Object
    - passes: a list of OverheadPass objects
    """

    def __init__(self, city: City, *args):
        """
        Initializes a CityOverheadTimes object which stores the various
        times the ISS will pass over a city.
        :param city: a City object
        :param args: a list of dictionaries with "duration" and
        "risetime" keys
        """
        self.city = city
        self.passes = []
        # for arg in args:
        #     self.passes.append(OverheadPassEvent(**arg))
        for arg in args:
            for a in arg:
                self.passes.append(OverheadPassEvent(**a))

    def __str__(self):
        times = []
        for iss_pass in self.passes:
            times.append(str(iss_pass))
        times = '\n'.join(times)
        return f"The ISS will pass over {self.city.city_name} " \
               f"{len(self.passes)} times. The times are: \n {times}"


class ISSDataRequest:
    """
    A wrapper for accessing the Open Notify API's iss-pass endpoint.
    This endpoint takes the location (latitude and longitude) and
    returns data about the number of times and the exact times that the
    ISS space station will be directly overhead that location.
    """

    # The url to the overhead pass endpoint form the Open notify API
    OPEN_NOTIFY_OVERHEAD_PASS_URL = "http://api.open-notify.org/iss-pass.json"

    @classmethod
    def create_url(cls, lat, lng):
        return f"{ISSDataRequest.OPEN_NOTIFY_OVERHEAD_PASS_URL}?lat=" \
               f"{lat}&lon={lng}"

    # http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON
    @classmethod
    def get_overhead_pass(cls, city: City) -> CityOverheadTimes:
        url = ISSDataRequest.create_url(city.lat, city.lng)
        response = requests.get(url)
        return response.json()
        # jprint(response.json())


def main():
    db = CityDatabase("city_locations_test.xlsx")
    for city in db.city_db:
        json = ISSDataRequest.get_overhead_pass(city)
        CityOverheadTimes(city, json)


if __name__ == "__main__":
    main()
