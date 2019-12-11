"""tests Google Maps's API response with mock"""


import urllib.request

from app.utils.api_google_maps import GoogleMapsObject


class TestGoogleMapsApi:
    """initializes test class for the Google Maps API with its attributes and methods"""

    def __init__(self):
        self.keyword = "tour Eiffel"
        self.google_maps_object = GoogleMapsObject(self.keyword)

    def test_search(self, monkeypatch):
        """tests google maps search and asserts results"""

        results = {'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                   'longitude': 2.2944813, 'latitude': 48.85837009999999}

        def mockreturn():
            """returns mock results"""

            return results

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.google_maps_object.search_address() == results
