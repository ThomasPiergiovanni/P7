"""Place module.
"""
from configuration.config import LOCATION_BIAS
from configuration.env import Env
from grandpy.apiclients.api_generic import ApiGeneric


class Place(ApiGeneric):
    """ Place class
    """
    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.name = ""
        self.address = ""

    def set_request(self, parsed_chain):
        """Method that sets endpoint and parameters for request to Place
        API.
        """
        self.endpoint = (
                "https://maps.googleapis.com/maps/api/place/"
                "findplacefromtext/json?")
        self.parameters = {
                "input": parsed_chain,
                "inputtype": "textquery",
                "fields": "place_id,name,formatted_address",
                "locationbias": LOCATION_BIAS,
                "key": Env.GG_API_KEY_BACKEND}

    def set_attribute(self):
        """Method that sets attributes values with informations
        from the api response.
        """
        if self.response["status"] == "OK":
            self.status = True
            candidates = self.response["candidates"]
            for candidate in candidates:
                self.place_id = candidate["place_id"]
                self.name = candidate["name"]
                self.address = candidate["formatted_address"]
