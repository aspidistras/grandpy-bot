"""uses Media Wiki's API to get the information on the user input"""

import json
import requests

from constants import URL_WIKI


class MediaWikiObject:
    """initializes MediaWikiObject with its attributes and methods to determine
    whether API search is ok and if so get the data"""

    def __init__(self, location):
        self.location = location
        self.url = URL_WIKI.format(location)
        self.request = requests.get(self.url)
        self.result = json.loads(self.request.text)
        self.data = dict()

    def search_is_ok(self):
        """checks if a Wikipedia page for the keywords can be found"""

        query = self.result["query"]
        pages = query["pages"]
        if "missing" in pages[0]:  # if the page requested doesn't exist
            return None

        return 1

    def search_info(self):
        """goes through the result to put into a dictionary the page content and link"""

        query = self.result["query"]
        pages = query["pages"]
        self.data["content"] = pages[0]["extract"]
        self.data["link"] = "https://fr.wikipedia.org/?curid={}".format(pages[0]["pageid"])
        return self.data

