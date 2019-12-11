""""tests parsing a sentence into words then into keywords"""


from app.utils.parser import Parser


class TestParser:
    """initializes test class for the parser with its attributes and method"""

    def __init__(self):
        self.sentence = "Est-ce que tu connais l'adresse de la tour Eiffel ?"
        self.parser = Parser(self.sentence)
        
    def test_parser(self):
        """tests parsing a sentence ans asserts results"""

        words_result = ["Est", "ce", "que", "tu", "connais", "l", "adresse", "de", "la", "tour",
                        "Eiffel", "?"]
        assert self.parser.sentence_to_words() == words_result

        keywords_result = ["tour", "Eiffel"]
        assert self.parser.words_to_keywords() == keywords_result
