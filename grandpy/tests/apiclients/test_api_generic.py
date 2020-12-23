# pylint: disable=too-few-public-methods
"""Test Api Generic module
"""
from grandpy.apiclients.api_generic import ApiGeneric


class EmulateGetRequests:
    """Class emulating requests lib get object
    """
    def __init__(self, endpoint=None, params=None):
        self.endpoint = endpoint
        self.params = params
        self.response = None

    def json(self):
        """Method returning a json object
        """
        return self.response


def test_get_request_with_reponse_is_true(monkeypatch):
    """Method that test get_request method returning reponse is True
    """
    class TrueResponse(EmulateGetRequests):
        """Class emulating requests lib get object and returning
        reponse is True.
        """
        def __init__(self, endpoint=None, params=None):
            super().__init__(endpoint=None, params=None)

        def json(self):
            """Method returning a json object with response sets to True
            """
            self.response = True
            return self.response

    monkeypatch.setattr("requests.get", TrueResponse)
    api_generic = ApiGeneric()
    api_generic.get_request()
    assert api_generic.response is True


def test_get_response_is_false(monkeypatch):
    """Method that test get_request method returning reponse is False
    """
    class FalseResponse(EmulateGetRequests):
        """Class emulating requests lib get object and returning
        reponse is True.
        """
        def __init__(self, endpoint=None, params=None):
            super().__init__(endpoint=None, params=None)

        def json(self):
            """Method returning a json object with response attribute sets to
            False.
            """
            self.response = False
            return self.response

    monkeypatch.setattr("requests.get", FalseResponse)
    api_generic = ApiGeneric()
    api_generic.get_request()
    assert api_generic.response is False
