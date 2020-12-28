# pylint: disable=too-few-public-methods
"""Program environnment variable module
"""
import os


class Env:
    """Environnement variable class
    """
    # DESCRIPTION: Variable stating whether the programm is deployed locally
    # or not.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: False"
    # CUSTOM SETTINGS: You can replace the default setting depending on
    # the app usage.
    LOCAL = True

    # DESCRIPTION: Secret key required for proper Flask usage.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("SECRET_KEY")
    # CUSTOM SETTINGS: You need to create environnment variable of that name,
    # i.e.SECRET_KEY, with your a secret value(only known to you).
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # DESCRIPTION: Google API key required for usage of Google APIs
    # (Backend calls).
    # is not restricted
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("GG_API_KEY")
    # CUSTOM SETTINGS: You need to create an environnment variable of that
    # name in your system i.e."GG_API_KEY" and with the value of an API key
    # provided by Google.That key must not be restircted on Google API
    # Plateform. To get a Google API key or for more info on Google APIs,
    # please check "https://developers.google.com/maps/gmp-get-started".
    GG_API_KEY_BACKEND = os.environ.get("GG_API_KEY")

    # DESCRIPTION: Google API key for usage of Google Map API (Backend calls).
    # This key must be restricted to its referent (http) if deployed
    # on the web.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS(if deployment is done locally):
    #       os.environ.get("GG_API_KEY")
    # DEFAULT SETTINGS(if deployment is done on web):
    #       os.environ.get("GG_API_KEY_RESTRICTED")
    # CUSTOM SETTINGS: You need to create a environnment variables of those
    # name in your system i.e."GG_API_KEY" and "GG_API_KEY_RESTRICTED"
    # with the value of an API key provided by Google."GG_API_KEY" don't need
    # to be restircted on Google API Plateform but "GG_API_KEY_RESTRICTED"
    # must. This "GG_API_KEY_RESTRICTED" key is the one used on your
    # production environnment.
    # To get a Google API key or for more info on Google APIs, please
    # check "https://developers.google.com/maps/gmp-get-started".
    if LOCAL:
        GG_API_KEY_FRONTEND = os.environ.get("GG_API_KEY")
    else:
        GG_API_KEY_FRONTEND = os.environ.get("GG_API_KEY_RESTRICTED")
