"""uses Google Maps'API to get the address related to the location"""


import json
import requests

from constants import URL_MAPS, GOOGLE_MAPS_KEY


class GoogleMapsObject:

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = URL_MAPS.format(self.keyword, GOOGLE_MAPS_KEY)
        self.request = requests.get(self.url)
        self.result = json.loads(self.request.text)
        self.status = self.result["status"]
        self.data = dict()

    def search_is_ok(self):
        if self.status == "OK":
            return 1
        else:
            return None

    def search_address(self):
        data = self.result["results"]
        self.data["address"] = data[0]["formatted_address"]
        self.data["longitude"] = data[0]["geometry"]["location"]["lng"]
        self.data["latitude"] = data[0]["geometry"]["location"]["lat"]
        print(self.data)
        return self.data
