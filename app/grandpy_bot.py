from app.logic.api_media_wiki import MediaWikiObject
from app.logic.api_google_maps import GoogleMapsObject
from app.logic.parser import Parser

import json


class GrandPyBot:

    def __init__(self, user_input):
        self.sentence = user_input
        self.keywords = None
        self.address = None
        self.location_data = None
        self.data = None

    def parse_sentence(self):
        parser = Parser(self.sentence)
        parser.sentence_to_words()
        self.keywords = parser.words_to_keywords()
        print(self.keywords)

    def get_location(self):
        keywords_string = '%20'.join(self.keywords)
        google_maps_object = GoogleMapsObject(keywords_string)
        if google_maps_object.search_is_ok() is 1:
            self.address = google_maps_object.search_address()
            print(self.address)
            return self.address
        else:
            return None

    def get_location_data(self):
        keywords_string = '%20'.join(self.keywords)
        media_wiki_object = MediaWikiObject(keywords_string)
        if media_wiki_object.search_is_ok() is 1:
            self.location_data = media_wiki_object.search_info()
            print(self.location_data)
        else:
            return None

    def return_data(self):
        self.parse_sentence()
        if self.get_location_data() or self.get_location():
            data = self.address + self.location_data
            self.data = json.dumps(data, ensure_ascii=False)
            return self.data
        else:
            return None


