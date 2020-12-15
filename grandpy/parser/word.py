# pylint: disable=too-few-public-methods


"""Word module
"""


class Word:
    """Word class
    """
    def __init__(self):
        self.index = None
        self.name = None
        self.enum = {
                "min_two": None,
                "min_one": None,
                "self": None,
                "plus_one": None,
                "plus_two": None,
                "plus_three": None}
