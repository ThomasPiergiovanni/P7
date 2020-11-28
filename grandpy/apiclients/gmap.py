"""Map module.
"""
import requests

from configuration.config import Config, LOCATION_BIAS


class Gmap:
    """
    """
    def __init__(self):
        self.config = Config()
        self.url = "https://www.google.com/maps/embed/v1/place?key=" + self.config.GG_API_KEY + "&q=France&zoom=5"

    def set_place_location(self, place_id):
        self.url = "https://www.google.com/maps/embed/v1/place?key=" + self.config.GG_API_KEY + "&q=place_id:" + place_id