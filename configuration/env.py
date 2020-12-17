# pylint: disable=too-few-public-methods
"""Program environnment variable module
"""
import os


class Env:
    """Environnement variable class
    """

    # DESCRIPTION: Variable stating whether the programm is deployed locally or
    # not
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: False"
    # CUSTOM SETTINGS: You must repalce the default "you-will-never-guess"
    # with a string of yours own knowledge.
    LOCAL = True

    # DESCRIPTION: Secret key required for proper Flask usage.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("SECRET_KEY") or "you-will-never-guess"
    # CUSTOM SETTINGS: You must repalce the default "you-will-never-guess"
    # with a string of yours own knowledge.
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # DESCRIPTION: Google API key required for usage of Google APIs. This key
    # is not restricted
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: "xxxxxx"
    # CUSTOM SETTINGS: You must replace the default key with your own
    # google api key. Fore more informations, please check "https://developers
    # .google.com/maps/gmp-get-started".You also need to create an
    # environnment variable of that name and with the value provided by GG.
    GG_API_KEY = os.environ.get("GG_API_KEY_RESTRICTED")

    # DESCRIPTION: Google API key for usage of Google Map API. This key 
    # must be restricted to its server IP or referent (http) if deployed
    # on the web. 
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: "xxxxxx"
    # CUSTOM SETTINGS: You must replace the default key with your own
    # google api key. Fore more informations, please check 
    # "https://developers.google.com/maps/gmp-get-started".
    # You also need to create an environnment variable of that name
    # and with the value provided by GG. Note that if the app is used
    # localy, you'll use the
    GG_API_KEY_RESTRICTED = os.environ.get("GG_API_KEY_RESTRICTED")


