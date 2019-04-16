"""tests Google Maps's API response with mock"""

import urllib.request

from app.logic.api_google_maps import GoogleMapsObject


class TestGoogleMapsApi:

    def setup_method(self):
        self.keyword = "tour Eiffel"
        self.google_maps_object = GoogleMapsObject(self.keyword)

    def test_search(self, monkeypatch):
        results = {'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France', 'longitude': 2.2944813,
                   'latitude': 48.85837009999999}

        def mockreturn(request):
            return results

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.google_maps_object.search_address() == results





