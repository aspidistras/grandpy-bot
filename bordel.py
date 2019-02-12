import json
import requests
import urllib.request

from io import BytesIO



def __init__(self, location):
    self.location = location


def setup_method(self):
    self.location = "Cité Paradis"


def test_media_wiki_api(self, monkeypatch):
    results = [{
        "title": "OpenClassrooms"
    }]

    def mockreturn(request):
        return BytesIO(self.results_dumps.encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert search_media_wiki(self.location) is not None



def a():
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=OpenClassrooms&utf8="
    request = requests.get(url)
    result = json.loads(request.text)
    name = result["query"]
    print(name)
    search = name["search"]
    id = search[0]["pageid"]
    print(id)

    page = "https://fr.wikipedia.org/w/api.php?action=query&prop=revisions&" \
           "rvprop=content&format=json&formatversion=2&titles=OpenClassrooms"


a()


def b():
    url = "https://www.google.com/maps/search/?api=1&query=paris"
    request = requests.get(url)
    webbrowser.open(url)


b()