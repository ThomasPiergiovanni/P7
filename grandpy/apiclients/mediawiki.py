import requests

from configuration.config import Config

class MediaWiki:
    """
    """
    def __init__(self, parsed_string):
        self.config = Config()
        self.endpoint = "https://fr.wikipedia.org/w/api.php"
        self.parameters = {

                "action": "query",
                "format": "json",
                "prop": "extracts",
                "exintro" :0,
                "explaintext" :0 ,
                "redirects" : 1,
                "titles": parsed_string
                }
        self.response = None
        self.information = None
        self.status = False

    def get_mediawiki(self):
        """
        """
        try:
            response_api = requests.get(self.endpoint, params = \
                    self.parameters)
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
        """
        """
        try:
            for key in self.response["query"]["pages"].keys():
                self.status = True
                self.information = self.response["query"]["pages"]\
                        [key]["extract"]
        except KeyError as error:
            self.status = False


