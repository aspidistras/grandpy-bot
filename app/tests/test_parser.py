""""tests parsing a sentence"""

from ..logic import parser as script


class TestParser:

    def setup_method(self):
        self.sentence = "Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.words = ["Est", "ce", "que", "tu", "connais", "l'", "adresse",
                      "d'", "OpenClassrooms", "?"]
        self.keywords = ["adresse", "OpenClassrooms" ]
        
    def test_sentence_to_words(self):
        assert script.sentence.sentence_to_words(self.sentence) == self.words

    def test_keywords(self):
        assert script.words_to_keywords(self.words) == self.keywords


