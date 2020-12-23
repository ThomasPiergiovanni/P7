# pylint: disable=too-few-public-methods
"""Test Place module
"""
from grandpy.apiclients.place import Place


def test_set_attribute_with_response_returning_place():
    """Function that test set_attribute method by providing a
    response returning an existing object
    """
    response_ok = {
        'candidates': [{
            'formatted_address': '92340 Bourg-la-Reine, France',
            'name': 'Bourg-la-Reine',
            'place_id': 'ChIJBY5REypx5kcRgD6LaMOCCwQ'}],
        'status': 'OK'}
    place = Place()
    place.response = response_ok
    place.set_attribute()
    assert place.status is True
    assert place.place_id == "ChIJBY5REypx5kcRgD6LaMOCCwQ"
    assert place.name == "Bourg-la-Reine"
    assert place.address == "92340 Bourg-la-Reine, France"


def test_set_attribute_with_response_returning_no_place():
    """Function that test set_attribute method by providing a
    response returning an unexisting object
    """
    response_nok = {
            'candidates': [],
            'status': 'ZERO_RESULTS'}
    place = Place()
    place.response = response_nok
    place.set_attribute()
    assert place.status is not True
    assert place.place_id == ""
    assert place.name == ""
    assert place.address == ""
