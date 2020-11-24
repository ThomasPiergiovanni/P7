import requests

from configuration.config import Config

class MediaWiki:
    """
    """
    def __init__(self):
        self.config = Config()
        self.endpoint = "https://fr.wikipedia.org/w/api.php"
        self.parameters = {

                "action": "query",
                "format": "json",
                "prop": "extracts",
                "exintro" :0,
                "explaintext" :0 ,
                "redirects" : 1,
                "titles": "Bourg-la-Reine"
                }
        self.mediawiki_answer = None
        self.information = None

    def get_mediawiki(self):
        """
        """
        try:
            response_api = requests.get(self.endpoint, params = self.parameters)
            self.mediawiki_answer = response_api.json()

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
        # for key, value in self.mediawiki_answer.iteritems():
        #     print(key, value)

        pages = self.mediawiki_answer["query"]["pages"]
        for key in pages.keys():
            page_id = key
            print(page_id)
        self.information = self.mediawiki_answer["query"]["pages"][page_id]["extract"]
        
        print(self.information)
        # for candidate in candidates:
        #     self.place_id = candidate["place_id"]
        #     self.name = candidate["name"]
        #     self.address = candidate["formatted_address"]
        #     latitude = candidate["geometry"]["location"]["lat"]
        #     longitude = candidate["geometry"]["location"]["lng"]
        #     print(self.place_id)
        #     print(self.name)