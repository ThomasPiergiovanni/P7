"""Connection manager module.
"""
import requests

from configuration.config import Config


class GooglePlaces:
    """
    """
    def __init__(self, parsed_string):
        self.config = Config()
        self.endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        self.input = None
        # self.inputtype = "textquery"
        # self.fields = "formatted_address,name"
        # self.locationbias = "rectangle:48.7783,2.3129|48.7801,2.3168"

        self.parameters = {
                "input" : parsed_string,
                "inputtype" : "textquery",
                "fields": "name,formatted_address,geometry,types",
                "locationbias": "rectangle:48.7783,2.3129|48.7801,2.3168",
                "key" : self.config.GG_API_KEY
                }

        self.places_api_answer = None
        self.address = ""

    def get_places(self):

        try:
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

    def get_attribute(self):
        # response = {'candidates': 
        #                 [
        #                     {'formatted_address': '1 bis Rue René Roeckel, 92340 Bourg-la-Reine, France',
        #                     'geometry': {'location': {'lat': 48.779397, 'lng': 2.3149264}, 
        #                                 'viewport': {'northeast': {'lat': 48.78074967989272, 'lng': 2.316450729892722},
        #                                             'southwest': {'lat': 48.77805002010727, 'lng': 2.313751070107277}
        #                                             }},
        #                     'name': 'Les Caves Nysa',
        #                     'types': ['liquor_store', 'food', 'point_of_interest', 'store', 'establishment']
        #                     }
        #                 ],
        #             'status': 'OK'}


        candidates = self.places_api_answer["candidates"]
        for candidate in candidates:
            name = candidate["name"]
            self.address = candidate["formatted_address"]
            latitude = candidate["geometry"]["location"]["lat"]
            longitude = candidate["geometry"]["location"]["lng"]
            print(name)
            print(self.address)
            print(latitude)
            print(longitude)



