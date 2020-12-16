# pylint: disable=too-few-public-methods
"""Program environnment variable module
"""
import os


class Env:
    """Environnement variable class
    """
    # DESCRIPTION: Secret key required for proper Flask usage.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("SECRET_KEY") or "you-will-never-guess"
    # CUSTOM SETTINGS: You must repalce the default "you-will-never-guess"
    # with a string of yours own knowledge.
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # DESCRIPTION: Google API key required for usage of google APIs.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: "xxxxxx"
    # CUSTOM SETTINGS: You must replace the default key with your own
    # google api key. Fore more informations, please check "https://developers
    # .google.com/maps/gmp-get-started"
    GG_API_KEY_RESTRICTED = os.environ.get("GG_API_KEY_RESTRICTED")

    # DESCRIPTION: Google API key required for usage of google APIs.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: "xxxxxx"
    # CUSTOM SETTINGS: You must replace the default key with your own
    # google api key. Fore more informations, please check "https://developers
    # .google.com/maps/gmp-get-started"
    GG_API_KEY = os.environ.get("GG_API_KEY")
