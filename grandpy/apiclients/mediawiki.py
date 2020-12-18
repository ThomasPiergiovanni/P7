"""MediaWiki module.
"""
import requests

from configuration.config import CONNECTION_ERROR


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
        self.wikipedia_url = None
        self.status = False

    def get_mediawiki(self):
        """Method that makes a parameterized request to Media WIki API and get
        a response object back.
        """
        try:
            response_api = requests.get(self.endpoint, params=self.parameters)
            self.response = response_api.json()
        except requests.ConnectionError:
            print(CONNECTION_ERROR)
        except requests.Timeout:
            print(CONNECTION_ERROR)

    def set_attribute(self, parsed_chain):
        """Method that sets attributes values with informations
        from the api response.
        """
        try:
            for key in self.response["query"]["pages"].keys():
                self.status = True
                self.information = (
                        self.response["query"]["pages"][key]["extract"])
                self.wikipedia_url = "https://fr.wikipedia.org/wiki/" + parsed_chain
        except KeyError:
            self.status = False
