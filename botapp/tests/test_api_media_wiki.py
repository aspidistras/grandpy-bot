"""tests Media Wiki's API response"""


import urllib
import unittest
import re

from botapp.utils.api_media_wiki import MediaWikiObject


class TestMediaWikiAPI(unittest.TestCase):
    """initializes test class for the Media Wiki API with its attributes and methods"""

    def setUp(self):
        self.keyword = "tour Eiffel"
        self.media_wiki_object = MediaWikiObject(self.keyword)
        self.link_regex = "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

    def test_search(self):
        """tests media wiki search and asserts results"""

        response = self.media_wiki_object.search_info()

        assert response["content"] is not None
        assert re.search(self.link_regex, response["link"])


if __name__ == '__main__':
    unittest.main()
