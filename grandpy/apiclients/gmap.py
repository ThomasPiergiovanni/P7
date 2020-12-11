"""Map module.
"""
from configuration.env import Env


class Gmap:
    """
    """
    def __init__(self):
        self.env = Env()
        self.url = "https://www.google.com/maps/embed/v1/place?key=" +\
                self.env.GG_API_KEY + "&q=France&zoom=5"

    def set_place_location(self, place_id):
        """
        """
        self.url = "https://www.google.com/maps/embed/v1/place?key=" +\
                self.env.GG_API_KEY + "&q=place_id:" + place_id