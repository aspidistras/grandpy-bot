"""tests Media Wiki's API response with mock"""


class TestMediaWikiAPI:

    def setup_method(self):
        location = "Cité Paradis"
        self.media_wiki_object = MediaWikiObject(location)

    def test_search_is_ok(self):
        assert self.media_wiki_object.search_is_ok() is not None

    def test_search_info(self):
        assert self.media_wiki_object.search_info() == \
               "La cité Paradis est une voie publique située " \
               "dans le 10e arrondissement de Paris."
