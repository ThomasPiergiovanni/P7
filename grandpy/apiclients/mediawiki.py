"""MediaWiki module.
"""
from grandpy.apiclients.api_generic import ApiGeneric

class MediaWiki(ApiGeneric):
    """ MediaWiki class
    """
    def __init__(self):
        super().__init__()
        self.information = None
        self.wikipedia_url = None

    def set_request(self, parsed_chain):
        """Method that sets endpoint and parameters for request to Media Wiki
        API.
        """
        self.endpoint = "https://fr.wikipedia.org/w/api.php"
        self.parameters = {
                "action": "query",
                "format": "json",
                "prop": "extracts",
                "exintro": 0,
                "explaintext": 0,
                "redirects": 1,
                "titles": parsed_chain}

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
