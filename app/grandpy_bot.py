from app.logic.api_media_wiki import MediaWikiObject
from app.logic.api_google_maps import GoogleMapsObject
from app.logic.parser import Parser

import json


class GrandPyBot:

    def __init__(self, user_input):
        self.sentence = user_input
        self.keywords = None
        self.location_details = ""
        self.location_data = ""
        self.data = dict()

    def parse_sentence(self):
        parser = Parser(self.sentence)
        parser.sentence_to_words()
        self.keywords = parser.words_to_keywords()

    def get_location_details(self):
        keywords_string = '%20'.join(self.keywords)
        google_maps_object = GoogleMapsObject(keywords_string)
        if google_maps_object.search_is_ok() is 1:
            self.location_details = google_maps_object.search_address()
            return True
        else:
            return False

    def get_location_data(self):
        keywords_string = '%20'.join(self.keywords)
        media_wiki_object = MediaWikiObject(keywords_string)
        if media_wiki_object.search_is_ok() is 1:
            self.location_data = media_wiki_object.search_info()
            return True
        else:
            return False

    def return_data(self):
        self.parse_sentence()
        if self.get_location_details() and self.get_location_data():
            self.data["locationDetails"] = self.location_details
            self.data["locationData"] = self.location_data
            return self.data
        else:
            return None
