"""Test Place module
"""
from grandpy.apiclients.place import Place


def test_get_place_with_an_existing_place(monkeypatch):
    """Method that test get_place method by providing an existing place
    """
    parsed_string_ok = "Bourg-la-Reine"
    response_ok = {
        'candidates': [{
            'formatted_address': '92340 Bourg-la-Reine, France',
            'name': 'Bourg-la-Reine',
            'place_id': 'ChIJBY5REypx5kcRgD6LaMOCCwQ'}],
        'status': 'OK'}

    class MockResponse:
        """MockResponse class
        """
        def __init__(self, endpoint, params=None):
            self.endpoint = endpoint
            self.params = params
            self.response = None

        def json(self):
            """Method returning a json object
            """
            self.response = response_ok
            return self.response

    monkeypatch.setattr("requests.get", MockResponse)
    place = Place(parsed_string_ok)
    place.get_place()
    assert place.place_api_answer["status"] == 'OK'


def test_get_place_an_unexisting_place(monkeypatch):
    """Method that test get_place method by providing an unexisting place
    """
    parsed_string_nok = "Brg-la-Rine"
    response_nok = {
            'candidates': [],
            'status': 'ZERO_RESULTS'}

    class MockResponse:
        """MockResponse class
        """
        def __init__(self, endpoint, params=None):
            self.endpoint = endpoint
            self.params = params
            self.response = None

        def json(self):
            """Method returning a json object
            """
            self.response = response_nok
            return self.response

    monkeypatch.setattr("requests.get", MockResponse)
    place = Place(parsed_string_nok)
    place.get_place()
    assert place.place_api_answer["status"] == 'ZERO_RESULTS'


def test_set_attribute_with_response_returning_place():
    """Function that test set_attribute method by providing a
    response returning an existing object
    """
    parsed_string_ok = "Bourg-la-Reine"
    response_ok = {
        'candidates': [{
            'formatted_address': '92340 Bourg-la-Reine, France',
            'name': 'Bourg-la-Reine',
            'place_id': 'ChIJBY5REypx5kcRgD6LaMOCCwQ'}],
        'status': 'OK'}
    place = Place(parsed_string_ok)
    place.place_api_answer = response_ok
    place.set_attribute()
    assert place.status is True
    assert place.place_id == "ChIJBY5REypx5kcRgD6LaMOCCwQ"
    assert place.name == "Bourg-la-Reine"
    assert place.address == "92340 Bourg-la-Reine, France"


def test_set_attribute_with_response_returning_no_place():
    """Function that test set_attribute method by providing a
    response returning an unexisting object
    """
    parsed_string_nok = "Brg-la-Rine"
    response_nok = {
            'candidates': [],
            'status': 'ZERO_RESULTS'}
    place = Place(parsed_string_nok)
    place.place_api_answer = response_nok
    place.set_attribute()
    assert place.status is False
    assert place.place_id == ""
    assert place.name == ""
    assert place.address == ""
