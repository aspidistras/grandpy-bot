"""uses Google Maps'API to get the address related to the user input"""


import json
import requests

from constants import URL_MAPS, GOOGLE_MAPS_KEY


class GoogleMapsObject:
    """initializes GoogleMapsObject with its attributes and methods to determine
    whether API search is ok and if so get the data"""

    def __init__(self, keywords):
        self.keywords = keywords
        self.url = URL_MAPS.format(self.keywords, GOOGLE_MAPS_KEY)
        self.request = requests.get(self.url)
        self.result = json.loads(self.request.text)
        self.status = self.result["status"]
        self.data = dict()

    def search_is_ok(self):
        """checks if request's status is OK"""

        if self.status == "OK":  # if the request was valid
            return 1

        return None

    def search_address(self):
        """goes through the result to put into a dictionary the address and location's geometry
        details and returns data"""

        data = self.result["results"]
        self.data["address"] = data[0]["formatted_address"]
        self.data["longitude"] = data[0]["geometry"]["location"]["lng"]
        self.data["latitude"] = data[0]["geometry"]["location"]["lat"]
        return self.data
