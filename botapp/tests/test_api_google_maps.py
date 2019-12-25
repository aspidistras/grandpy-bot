"""tests Google Maps's API response"""


import urllib.request
import unittest

from botapp.utils.api_google_maps import GoogleMapsObject


class TestGoogleMapsApi(unittest.TestCase):
    """initializes test class for the Google Maps API with its attributes and methods"""

    def setUp(self):
        self.keyword = "tour Eiffel"
        self.google_maps_object = GoogleMapsObject(self.keyword)

    def test_search(self):
        """tests google maps search and asserts results"""

        results = {'address': '5 Avenue Anatole France Champ de Mars, 75007 Paris, France',
                'longitude': 2.2944833, 'latitude': 48.8583698}

        assert self.google_maps_object.search_address() == results


if __name__ == '__main__':
  unittest.main()