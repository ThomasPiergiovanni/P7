"""Test Gmap module
"""
from configuration.env import Env
from grandpy.apiclients.gmap import Gmap


class TestGmap:
    """ Test Gmap class
    """
    def test_set_place_location_with_place_id_provided(self):
        """Method that test set_place_location method with providing
        a place id
        """
        place_id = "ChIJLU7jZClu5kcR4PcOOO6p3I0"
        gmap = Gmap()
        gmap.set_place_location(place_id)
        assert gmap.url == (
                "https://www.google.com/maps/embed/v1/place?key=" +
                Env.GG_API_KEY + "&q=place_id:" + place_id)
