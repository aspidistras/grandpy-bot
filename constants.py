"""initializes the constants needed throughout the app"""

import os

URL_WIKI = "https://fr.wikipedia.org/w/api.php?action=query" \
            "&prop=extracts&explaintext=true&exsectionformat=plain" \
            "&exsentences=5&format=json&formatversion=2&titles={}"

URL_MAPS = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"


GOOGLE_MAPS_KEY = os.environ['GOOGLE_MAPS_KEY']
