""" test google places module
"""
from grandpy.apiclients.google_places import GooglePlaces


class TestGooglePlaces:

    def test_get_places_is_successfull(self, monkeypatch):
        t_parsed_string_ok = "Bourg-la-Reine"
        t_response_ok = {
            'candidates': [{
                'formatted_address': '92340 Bourg-la-Reine, France',
                'name': 'Bourg-la-Reine',
                'place_id': 'ChIJBY5REypx5kcRgD6LaMOCCwQ'}],
            'status': 'OK'}
        class MockResponse:
            def __init__(self, endpoint, params = None):
                pass

            def json(self):
                return t_response_ok
               
        monkeypatch.setattr("requests.get", MockResponse)
        place = GooglePlaces(t_parsed_string_ok)
        place.get_places()
        assert place.places_api_answer["status"] == 'OK'

    def test_get_places_is_not_successfull(self, monkeypatch):
        t_parsed_string_nok = "Brg-la-Rine"
        t_response_nok = {
                'candidates': [],
                'status': 'ZERO_RESULTS'}


        class MockResponse:
            def __init__(self, endpoint, params = None):
                pass

            def json(self):
                return t_response_nok
               
        monkeypatch.setattr("requests.get", MockResponse)
        place = GooglePlaces(t_parsed_string_nok)
        place.get_places()
        assert place.places_api_answer["status"] == 'ZERO_RESULTS'
