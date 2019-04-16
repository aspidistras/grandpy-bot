""""tests parsing a sentence"""

from app.logic.parser import Parser


class TestParser:

    def setup_method(self):
        self.sentence = "Est-ce que tu connais l'adresse de la tour Eiffel ?"
        self.parser = Parser(self.sentence)
        
    def test_parser(self):
        words_result = ["Est", "ce", "que", "tu", "connais", "l", "adresse", "de", "la", "tour", "Eiffel", "?"]
        assert self.parser.sentence_to_words() == words_result

        keywords_result = ["tour", "Eiffel"]
        assert self.parser.words_to_keywords() == keywords_result


