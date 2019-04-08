"""parses the sentence typed by the user to get the keywords"""

import re
import json


class Parser:

    def __init__(self, sentence):

        self.sentence = sentence
        self.words = []
        self.keywords = []

    def sentence_to_words(self):
        delimiters = " ", ",", "-", ":", "'"
        regex_pattern = '|'.join(map(re.escape, delimiters))
        self.words = re.split(regex_pattern, self.sentence)

        for word in self.words:
            if word == "":
                self.words.remove(word)

    def words_to_keywords(self):
        with open("logic/stop_words.json", encoding="utf-8") as stop_words_file:
            print("a")
            stop_words = json.loads(stop_words_file.read())

        for word in self.words:
            if word not in stop_words:
                self.keywords.append(word)

        print(self.keywords)
        return self.keywords
