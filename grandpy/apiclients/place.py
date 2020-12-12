"""Place module.
"""
import requests

from configuration.config import LOCATION_BIAS
from configuration.env import Env


class Place:
    """ Place class
    """
    def __init__(self, parsed_chain):
        self.endpoint = (
                "https://maps.googleapis.com/maps/api/place/"
                "findplacefromtext/json?")
        self.parameters = {
                "input": parsed_chain,
                "inputtype": "textquery",
                "fields": "place_id,name,formatted_address",
                "locationbias": LOCATION_BIAS,
                "key": Env.GG_API_KEY
                }
        self.place_api_answer = None
        self.status = False
        self.place_id = ""
        self.name = ""
        self.address = ""

    def get_place(self):
        """Method that makes a parameterized request to Google
        Place API and get a response object back.
        """
        try:
            response_api = requests.get(self.endpoint, params=self.parameters)
            self.place_api_answer = response_api.json()
        except requests.ConnectionError:
            print(
                    "Un problème de connection est apparu. Ré-essaayez plus"
                    " tard ou contacter le propriétaire de l'application")
        except requests.Timeout:
            print(
                    "Un problème de connection est apparu. Ré-essaayez plus"
                    " tard ou contacter le propriétaire de l'application")

    def set_attribute(self):
        """Method that sets attributes values with informations
        from the api response.
        """
        if self.place_api_answer["status"] == "OK":
            self.status = True
            candidates = self.place_api_answer["candidates"]
            for candidate in candidates:
                self.place_id = candidate["place_id"]
                self.name = candidate["name"]
                self.address = candidate["formatted_address"]
