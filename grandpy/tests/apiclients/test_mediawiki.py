"""Test mediawiki module
"""
from grandpy.apiclients.mediawiki import MediaWiki


class TestMediaWiki:
    def test_get_mediawiki_when_exists(self, monkeypatch):
        place_ok = "Bourg-la-Reine"
        response_ok = {
                'batchcomplete': '',
                'query': {
                    'pages': {
                        '80897': {
                            'pageid': 80897,
                            'ns': 0,
                            'title': 'Bourg-la-Reine',
                            'extract': "Bourg-la-Reine est une commune française du département des Hauts-de-Seine en région Île-de-France, dans l'arrondissement d'Antony, au sud de Paris. \nElle fait partie de la métropole du Grand Paris créée en 2016.\n\n"
                        }}}}
        class MockResponse:
            def __init__(self, endpoint, params = None):
                pass

            def json(self):
                return response_ok
               
        monkeypatch.setattr("requests.get", MockResponse)
        mediawiki = MediaWiki(place_ok)
        mediawiki.get_mediawiki()
        assert mediawiki.response == response_ok


    def test_get_mediawiki_when_does_not_exists(self, monkeypatch):
        place_nok = "Brg-la-Rine"
        response_nok = {
                'batchcomplete': '',
                'query':{
                    'pages':{
                        '-1': {
                            'ns': 0,
                            'title': 'OpenClasdsdsrooms',
                            'missing': ''
                            }}}}
        class MockResponse:
            def __init__(self, endpoint, params = None):
                pass

            def json(self):
                return response_nok
               
        monkeypatch.setattr("requests.get", MockResponse)
        mediawiki = MediaWiki(place_nok)
        mediawiki.get_mediawiki()
        assert mediawiki.response == response_nok

    def test_set_attribute_when_exist(self):

        place_ok = "Bourg-la-Reine"
        response_ok = {
                'batchcomplete': '',
                'query': {
                    'pages': {
                        '80897': {
                            'pageid': 80897,
                            'ns': 0,
                            'title': 'Bourg-la-Reine',
                            'extract': "Bourg-la-Reine est une commune française du département des Hauts-de-Seine en région Île-de-France, dans l'arrondissement d'Antony, au sud de Paris. \nElle fait partie de la métropole du Grand Paris créée en 2016.\n\n"
                        }}}}
        mediawiki = MediaWiki(place_ok)
        mediawiki.response = response_ok
        mediawiki.set_attribute()
        assert mediawiki.status == True
        assert mediawiki.information == "Bourg-la-Reine est une commune française du département des Hauts-de-Seine en région Île-de-France, dans l'arrondissement d'Antony, au sud de Paris. \nElle fait partie de la métropole du Grand Paris créée en 2016.\n\n"

    def test_set_attribute_when_does_not_exist(self):

        place_nok = "Brg-la-Rine"
        response_nok = {
                'batchcomplete': '',
                'query':{
                    'pages':{
                        '-1': {
                            'ns': 0,
                            'title': 'OpenClasdsdsrooms',
                            'missing': ''
                            }}}}
        mediawiki = MediaWiki(place_nok)
        mediawiki.response = response_nok
        mediawiki.set_attribute()
        assert mediawiki.status == False
        assert mediawiki.information == None

