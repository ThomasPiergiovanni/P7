"""Test Api Generic module
"""
from grandpy.apiclients.api_generic import ApiGeneric


class EmulateGetRequests:
    """Class emulating requests lib requests.get object
    """
    def __init__(self, endpoint=None, params=None):
        self.endpoint = endpoint
        self.params = params
        self.response = None

    def json(self):
        """Method returning a json object
        """
        return self.response


def test_get_response_is_true(monkeypatch):
    """Method that test get_response method for requests to APIs
    by providing  response is True
    """
    class TrueResponse(EmulateGetRequests):
        """Class emulating requests lib requests.get object with an existing
        reposnse
        """
        def __init__(self, endpoint=None, params=None):
            super().__init__(endpoint=None, params=None)

        def json(self):
            self.response = True
            return self.response
   
    monkeypatch.setattr("requests.get", TrueResponse)
    api_generic = ApiGeneric()
    api_generic.get_response()
    assert api_generic.response == True


def test_get_response_is_false(monkeypatch):
    """Method that test get_response method for requests to APIs
    by providing response is False
    """
    class FalseResponse(EmulateGetRequests):
        """Class emulating requests lib requests.get object with an unexisting
        response.
        """
        def __init__(self, endpoint=None, params=None):
            super().__init__(endpoint=None, params=None)

        def json(self):
            self.response = False
            return self.response

    monkeypatch.setattr("requests.get", FalseResponse)
    api_generic = ApiGeneric()
    api_generic.get_response()
    assert api_generic.response == False
