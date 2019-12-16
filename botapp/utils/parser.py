"""parses the sentence typed by the user to get the keywords"""

import re
import json


class Parser:
    """initiates Parser object with its attributes and methods to break the user input into words
    and then keywords"""

    def __init__(self, sentence):

        self.sentence = sentence
        self.words = list()
        self.keywords = list()

    def sentence_to_words(self):
        """extracts words from sentence and puts them into a list"""

        delimiters = " ", ",", "-", ":", "'"
        regex_pattern = '|'.join(map(re.escape, delimiters))  # to suppress delimiters
        self.words = re.split(regex_pattern, self.sentence)

        for word in self.words:
            if word == "":
                self.words.remove(word)

        return self.words

    def words_to_keywords(self):
        """extracts keywords from words and puts them into a list"""

        with open("botapp/utils/stop_words.json", encoding="utf-8") as stop_words_file:
            # open json file with stop words in order to parse
            stop_words = json.loads(stop_words_file.read())

        for word in self.words:
            if word not in stop_words:
                self.keywords.append(word)  # gathers keywords

        return self.keywords
