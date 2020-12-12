"""MediaWiki module.
"""
import requests


class MediaWiki:
    """ MediaWiki class
    """
    def __init__(self, parsed_chain):
        self.endpoint = "https://fr.wikipedia.org/w/api.php"
        self.parameters = {
                "action": "query",
                "format": "json",
                "prop": "extracts",
                "exintro": 0,
                "explaintext": 0,
                "redirects": 1,
                "titles": parsed_chain
                }
        self.response = None
        self.information = None
        self.status = False

    def get_mediawiki(self):
        """Method that makes a parameterized request to Media WIki API and get
        a response object back.
        """
        try:
            response_api = requests.get(self.endpoint, params=self.parameters)
            self.response = response_api.json()
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
        try:
            for key in self.response["query"]["pages"].keys():
                self.status = True
                self.information = (
                        self.response["query"]["pages"][key]["extract"])
        except KeyError:
            self.status = False
