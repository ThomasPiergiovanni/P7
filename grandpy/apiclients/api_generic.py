"""API Generic module.
"""

import requests


class ApiGeneric:
    """ApiGeneric class
    """
    def __init__(self):
        self.endpoint = None
        self.parameters = None
        self.response = None
        self.connection_failure = False
        self.status = None

    def get_response(self):
        """Method that makes a parameterized requests to APIs and get
        a response object back.
        """
        try:
            response_api = requests.get(self.endpoint, params=self.parameters)
            self.response = response_api.json()
        except (
                requests.ConnectionError,
                requests.Timeout) :
            self.connection_failure = True
