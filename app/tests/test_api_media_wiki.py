"""tests Media Wiki's API response with mock"""


import urllib

from app.utils.api_media_wiki import MediaWikiObject


class TestMediaWikiAPI:
    """initializes test class for the Media Wiki API with its attributes and methods"""

    def __init__(self):
        self.keyword = "tour Eiffel"
        self.media_wiki_object = MediaWikiObject(self.keyword)

    def test_search(self, monkeypatch):
        """tests media wiki search and asserts results"""

        results = {'content': "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur "
                              "(avec antennes) située à Paris, à l’extrémité nord-ouest du parc du "
                              "Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. "
                              "Son adresse officielle est 5, avenue Anatole-France. Construite par "
                              "Gustave Eiffel et ses collaborateurs pour l’Exposition universelle "
                              "de Paris de 1889, et initialement nommée « tour de 300 mètres », "
                              "ce monument est devenu le symbole de la capitale française, "
                              "et un site touristique de premier plan : il s’agit du second site "
                              "culturel français payant le plus visité en 2011, avec 7,1 millions "
                              "de visiteurs dont 75 % d'étrangers en 2011, la cathédrale "
                              "Notre-Dame de Paris étant en tête des monuments à l'accès libre "
                              "avec 13,6 millions de visiteurs estimés mais il reste le monument "
                              "payant le plus visité au monde,. Depuis son ouverture au public, "
                              "elle a accueilli plus de 300 millions de visiteurs.\nD’une hauteur "
                              "de 312 mètres à l’origine, la tour Eiffel est restée le monument "
                              "le plus élevé du monde pendant quarante ans.",
                   'link': 'https://fr.wikipedia.org/?curid=1359783'}

        def mockreturn():
            """returns mock results"""
            return results

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.media_wiki_object.search_info() == results
