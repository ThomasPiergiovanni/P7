"""Connection manager module.
"""
import requests

from configuration.config import Config


class ConnectionManager:
    """
    """
    def __init__(self):
        self.config = Config()
        self.endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        self.input = "amarone"
        self.inputtype = "textquery"
        self.fields = "formatted_address,name"
        self.locationbias = "rectangle:48.7783,2.3129|48.7801,2.3168"

        self.parameters = {
                "input" : "amarone",
                "inputtype" : "textquery",
                "fields": "name,formatted_address,geometry,types",
                "locationbias": "rectangle:48.7783,2.3129|48.7801,2.3168",
                "key" : self.config.GG_API_KEY
                }

        # self.url_1 = self.endpoint\
        #         + "input="+ self.input\
        #         + "&inputtype=" + self.inputtype\
        #         + "&fields="+ self.fields\
        #         + "&locationbias="+ self.locationbias\
        #         + "&key=" + self.config.GG_API_KEY
        # print(self.url)
        # print(self.url_1)

        self.places_api_answer = None

    def get_places(self):

        try:
            # response_api = requests.get(
            #     self.url_1)
            response_api = requests.get(self.endpoint, params = self.parameters)
            self.places_api_answer = response_api.json()
            print(self.places_api_answer)

        except requests.ConnectionError:
            print(
                "Un problème de connection est apparu. Ré-essaayez plus"
                " tard ou contacter le propriétaire de l'application")
        except requests.Timeout:
            print(
                "Un problème de connection est apparu. Ré-essaayez plus"
                " tard ou contacter le propriétaire de l'application")
