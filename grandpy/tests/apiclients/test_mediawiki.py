"""Test mediawiki module
"""
from grandpy.apiclients.mediawiki import MediaWiki


def test_set_attribute_with_response_returning_place():
    """Function that test set_attribute method by providing a
    response returning an existing object
    """
    place_ok = "Bourg-la-Reine"
    response_ok = {
            'batchcomplete': '',
            'query': {
                'pages': {
                    '80897': {
                        'pageid': 80897,
                        'ns': 0,
                        'title': 'Bourg-la-Reine',
                        'extract': (
                                "Bourg-la-Reine est une commune française"
                                " du département des Hauts-de-Seine en"
                                " région Île-de-France, dans"
                                " l'arrondissement d'Antony, au sud de"
                                " Paris. \nElle fait partie de la"
                                " métropole du Grand Paris créée"
                                " en 2016.\n\n")}}}}
    mediawiki = MediaWiki()
    mediawiki.response = response_ok
    mediawiki.set_attribute(place_ok)
    assert mediawiki.status is True
    assert mediawiki.information == (
            "Bourg-la-Reine est une commune française du département"
            " des Hauts-de-Seine en région Île-de-France, dans"
            " l'arrondissement d'Antony, au sud de Paris. \nElle fait"
            " partie de la métropole du Grand Paris créée en 2016.\n\n")


def test_set_attribute_with_response_returning_no_place():
    """Function that test set_attribute method by providing a
    response returning an non existing object
    """
    place_nok = "Brg-la-Rine"
    response_nok = {
            'batchcomplete': '',
            'query': {
                'pages': {
                    '-1': {
                        'ns': 0,
                        'title': 'Brg-la-Rine',
                        'missing': ''
                        }}}}
    mediawiki = MediaWiki()
    mediawiki.response = response_nok
    mediawiki.set_attribute(place_nok)
    assert mediawiki.status is not True
    assert mediawiki.information is None
