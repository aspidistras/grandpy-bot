"""tests Google Maps's API response with mock"""


class TestGoogleMapsApi:

    def setup_method(self):
        keyword = "OpenClassrooms"
        self.google_maps_object = GoogleMapsObject(keyword)

    def test_search_is_ok(self):
        assert self.google_maps_object.search_is_ok() is not None

    def test_search_address(self):
        assert self.google_maps_object.search_address() == "7 Cité Paradis"





