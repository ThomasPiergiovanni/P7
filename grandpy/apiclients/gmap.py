"""Map module.
"""
from configuration.config import COUNTRY
from configuration.env import Env


class Gmap:
    """
    """
    def __init__(self):
        self.url = "https://www.google.com/maps/embed/v1/place?key=" +\
                Env.GG_API_KEY + "&q=" + COUNTRY + "&zoom=5"

    def set_place_location(self, place_id):
        """
        """
        self.url = "https://www.google.com/maps/embed/v1/place?key=" +\
                Env.GG_API_KEY + "&q=place_id:" + place_id