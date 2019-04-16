"""parses the sentence typed by the user to get the keywords"""

import re
import json


class Parser:

    def __init__(self, sentence):

        self.sentence = sentence
        self.words = list()
        self.keywords = list()

    def sentence_to_words(self):
        delimiters = " ", ",", "-", ":", "'"
        regex_pattern = '|'.join(map(re.escape, delimiters))
        self.words = re.split(regex_pattern, self.sentence)

        for word in self.words:
            if word == "":
                self.words.remove(word)

        return self.words

    def words_to_keywords(self):
        with open("app/logic/stop_words.json", encoding="utf-8") as stop_words_file:
            stop_words = json.loads(stop_words_file.read())

        for word in self.words:
            if word not in stop_words:
                self.keywords.append(word)

        return self.keywords


a = Parser("Est-ce que tu connais l'adresse de la tour Eiffel ?")
a.sentence_to_words()
print(a.words)
print(a.words_to_keywords())
