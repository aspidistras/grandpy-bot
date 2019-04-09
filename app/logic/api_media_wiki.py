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
        self.content = None

    def search_is_ok(self):
        query = self.result["query"]
        pages = query["pages"]
        if "missing" in pages[0]:
            return None
        else:
            return 1

    def search_info(self):
        print(self.url)
        query = self.result["query"]
        pages = query["pages"]
        self.content = pages[0]["extract"]
        return self.content
