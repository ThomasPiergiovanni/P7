# pylint: disable=too-few-public-methods


"""Test mediawiki module
"""


from grandpy.apiclients.mediawiki import MediaWiki


def test_get_mediawiki_with_an_existing_place(monkeypatch):
    """Method that test get_mediawiki method by providing a valid place
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
                                "Bourg-la-Reine est une commune"
                                "française du département des"
                                " Hauts-de-Seine en région Île-de-France,"
                                " dans l'arrondissement d'Antony, au sud "
                                "de Paris. \nElle fait partie de la "
                                "métropole du Grand Paris créée "
                                "en 2016.\n\n")}}}}

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
    mediawiki = MediaWiki(place_ok)
    mediawiki.get_mediawiki()
    assert mediawiki.response == response_ok


def test_get_mediawiki_with_an_unexisting_place(monkeypatch):
    """Function that test get_mediawiki method by providing a not
    valid place.
    """
    place_nok = "OpenClasdsdsrreoms"
    response_nok = {
            'batchcomplete': '',
            'query': {
                'pages': {
                    '-1': {
                        'ns': 0,
                        'title': 'OpenClasdsdsrooms',
                        'missing': ''
                        }}}}

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
    mediawiki = MediaWiki(place_nok)
    mediawiki.get_mediawiki()
    assert mediawiki.response == response_nok


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
    mediawiki = MediaWiki(place_ok)
    mediawiki.response = response_ok
    mediawiki.set_attribute()
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
    mediawiki = MediaWiki(place_nok)
    mediawiki.response = response_nok
    mediawiki.set_attribute()
    assert mediawiki.status is not True
    assert mediawiki.information is None
