"""uses Media Wiki's API to get the information on the address"""

import requests
import json

from constants import URL_WIKI


class MediaWikiObject:

    def __init__(self, location):
        self.location = location
        self.url = URL_WIKI.format(location)
        self.request = requests.get(self.url)
        self.result = json.loads(self.request.text)
        self.data = dict()

    def search_is_ok(self):
        query = self.result["query"]
        pages = query["pages"]
        if "missing" in pages[0]:
            return None
        else:
            return 1

    def search_info(self):
        query = self.result["query"]
        pages = query["pages"]
        self.data["content"] = pages[0]["extract"]
        self.data["link"] = "https://fr.wikipedia.org/?curid={}".format(pages[0]["pageid"])
        print(self.data)
        return self.data


a = MediaWikiObject("tour Eiffel")
a.search_info()