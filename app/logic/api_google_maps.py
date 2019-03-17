"""uses Google Maps'API to get the address related to the location"""


import json
import requests

from constants import URL_MAPS


class GoogleMapsObject:

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = URL_MAPS.format(self.keyword)
        self.request = requests.get(self.url)
        self.result = json.loads(self.request.text)
        self.status = self.result["status"]
        self.address = ""

    def search_is_ok(self):
        if self.status == "OK":
            return 1
        else:
            return None

    def search_address(self):
        data = self.result["results"]
        self.address = data[0]["formatted_address"]
        print(self.address)
        return self.address


a = GoogleMapsObject("a")
if a.search_is_ok() is not None:
    print("a")

a.search_address()
