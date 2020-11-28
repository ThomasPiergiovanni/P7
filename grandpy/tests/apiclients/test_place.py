""" test google places module
"""
from grandpy.apiclients.place import Place


class TestPlace:

    def test_get_place_when_exists(self, monkeypatch):
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
        place = Place(t_parsed_string_ok)
        place.get_place()
        assert place.place_api_answer["status"] == 'OK'

    def test_get_place_when_does_not_exists(self, monkeypatch):
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
        place = Place(t_parsed_string_nok)
        place.get_place()
        assert place.place_api_answer["status"] == 'ZERO_RESULTS'

    def test_set_attribute_when_place_exist(self):

        t_parsed_string_ok = "Bourg-la-Reine"
        t_response_ok = {
            'candidates': [{
                'formatted_address': '92340 Bourg-la-Reine, France',
                'name': 'Bourg-la-Reine',
                'place_id': 'ChIJBY5REypx5kcRgD6LaMOCCwQ'}],
            'status': 'OK'}
        t_place = Place(t_parsed_string_ok)
        t_place.place_api_answer = t_response_ok
        t_place.set_attribute()
        assert t_place.status == True
        assert t_place.place_id == "ChIJBY5REypx5kcRgD6LaMOCCwQ"
        assert t_place.name == "Bourg-la-Reine"
        assert t_place.address == "92340 Bourg-la-Reine, France"

    def test_set_attribute_when_place_doesnt_exist(self):

        t_parsed_string_nok = "Brg-la-Rine"
        t_response_nok = {
                'candidates': [],
                'status': 'ZERO_RESULTS'}
        t_place = Place(t_parsed_string_nok)
        t_place.place_api_answer = t_response_nok
        t_place.set_attribute()
        assert t_place.status == False
        assert t_place.place_id == ""
        assert t_place.name == ""
        assert t_place.address == ""
