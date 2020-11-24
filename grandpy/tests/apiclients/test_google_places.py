""" test google places module
"""
from grandpy.apiclients.google_places import GooglePlaces

class TestGooglePlaces:

        t_response = {'candidates': 
                        [
                            {'formatted_address': '1 bis Rue René Roeckel, 92340 Bourg-la-Reine, France',
                            'geometry': {'location': {'lat': 48.779397, 'lng': 2.3149264}, 
                                        'viewport': {'northeast': {'lat': 48.78074967989272, 'lng': 2.316450729892722},
                                                    'southwest': {'lat': 48.77805002010727, 'lng': 2.313751070107277}
                                                    }
                                        },
                            'name': 'Les Caves Nysa',
                            'types': ['liquor_store', 'food', 'point_of_interest', 'store', 'establishment']
                            }
                        ],
                    'status': 'OK'}

        def test_set_attribute_catches_the_correct_attribute(self):
                t_place = GooglePlaces()
                t_place.plaxes_api_answer = t_response
                t_place.set_attribute()
                assert t_place.address == t_response["candidates"][0]["formatted_address"]

