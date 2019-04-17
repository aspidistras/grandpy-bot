"""implements GrandPyBot class"""


from app.logic.api_media_wiki import MediaWikiObject
from app.logic.api_google_maps import GoogleMapsObject
from app.logic.parser import Parser


class GrandPyBot:
    """creates GrandPyBot class with its attributes and methods
    calling every function needed to return the bot's answer
    """

    def __init__(self, user_input):
        self.sentence = user_input
        self.keywords = None
        self.location_details = ""
        self.location_data = ""
        self.data = dict()  # to stock the data to return

    def parse_sentence(self):
        """creates Parser instance to get keywords"""
        parser = Parser(self.sentence)
        parser.sentence_to_words()
        self.keywords = parser.words_to_keywords()

    def get_location_details(self):
        """creates GoogleMapsObject instance to get the address and location details"""
        keywords_string = '%20'.join(self.keywords)  # to match url parameters' pattern
        google_maps_object = GoogleMapsObject(keywords_string)
        if google_maps_object.search_is_ok() == 1:
            self.location_details = google_maps_object.search_address()
            return True

        return False

    def get_location_data(self):
        """creates MediaWikiObject to get the information related to the obtained keywords"""
        capitalized_keywords = []
        for keyword in self.keywords:
            capitalized_keyword = keyword.capitalize()
            capitalized_keywords.append(capitalized_keyword) # to match url parameters' pattern
        keywords_string = '%20'.join(capitalized_keywords) # to match url parameters' pattern
        media_wiki_object = MediaWikiObject(keywords_string)
        if media_wiki_object.search_is_ok() == 1:
            self.location_data = media_wiki_object.search_info()
            return True

        return False

    def return_data(self):
        """returns a dictionary with every element needed to provide the user an answer"""
        self.parse_sentence()
        if self.get_location_details() and self.get_location_data():  # if the searches got through
            self.data["locationDetails"] = self.location_details
            self.data["locationData"] = self.location_data
            return self.data

        return None
