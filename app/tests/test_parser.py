""""tests parsing a sentence"""

from app.logic.parser import Parser


class TestParser:

    def setup_method(self):
        sentence = "Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.parser = Parser(sentence)
        
    def test_sentence_to_words(self):
        assert self.parser.sentence_to_words() == ["Est", "ce", "que", "tu",
                                                   "connais", "l'", "adresse",
                                                   "d'", "OpenClassrooms", "?"]

    def test_keywords(self):
        assert self.parser.keywords == ["OpenClassrooms"]


