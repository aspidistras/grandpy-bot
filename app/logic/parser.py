import re


class Parser:

    def __init__(self, sentence):

        self.sentence = sentence
        self.words = []
        self.keywords = []

    def sentence_to_words(self):
        delimiters = " ", ",", "-", ":"
        regex_pattern = '|'.join(map(re.escape, delimiters))
        self.words = re.split(regex_pattern, self.sentence)
        return self.words

    def words_to_keywords(self, words):
        pass
