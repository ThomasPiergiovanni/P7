"""Connection manager module.
"""
import requests

from configuration.config import LOCATION_BIAS

from configuration.env import Env


class Place:
    """
    """
    def __init__(self, parsed_string):
        self.env = Env()
        self.endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        self.parameters = {
                "input" : parsed_string,
                "inputtype" : "textquery",
                "fields": "place_id,name,formatted_address",
                "locationbias": "rectangle:48.7731,2.3056|48.7918,2.3307", #LOCATION_BIAS,
                "key" : self.env.GG_API_KEY
                }
        self.place_api_answer = None
        self.status = False
        self.place_id = ""
        self.name = ""
        self.address = ""

    def get_place(self):
        """
        """
        try:
            response_api = requests.get(self.endpoint, params = self.parameters)
            self.place_api_answer = response_api.json()
        except requests.ConnectionError as error:
            print(
                "Un problème de connection est apparu. Ré-essaayez plus"
                " tard ou contacter le propriétaire de l'application")
        except requests.Timeout:
            print(
                "Un problème de connection est apparu. Ré-essaayez plus"
                " tard ou contacter le propriétaire de l'application")

    def set_attribute(self):
        """
        """ 
        if self.place_api_answer["status"] == "OK":
            self.status = True
            candidates = self.place_api_answer["candidates"]
            for candidate in candidates:
                self.place_id = candidate["place_id"]
                self.name = candidate["name"]
                self.address = candidate["formatted_address"]
