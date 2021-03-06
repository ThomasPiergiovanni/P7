"""Google map module.
"""
from configuration.config import COUNTRY
from configuration.env import Env


class Gmap:
    """ Google map class
    """
    def __init__(self):
        self.gmap_url = None

    def set_default_location(self):
        """Method that sets the default url to get the default map.
        """
        self.gmap_url = (
                "https://www.google.com/maps/embed/v1/place?key=" +
                Env.GG_API_KEY_FRONTEND + "&q=" + COUNTRY + "&zoom=5")

    def set_place_location(self, place_id):
        """Method that sets the correct url to get the wanted map. place_id
        is obtained from Google Place API response. This after
        user question & parsing.
        """
        self.gmap_url = (
                "https://www.google.com/maps/embed/v1/place?key=" +
                Env.GG_API_KEY_FRONTEND + "&q=place_id:" + place_id)
