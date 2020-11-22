from flask import Flask
from configuration.config import Config

app = Flask(__name__)
# Crée une instance de la classe Flask.

app.config.from_object(Config)
# Je defini mon attribut config grace a lacd ap methode from object.
# qui va recupérer la classe de configuration Config

from website import routes 
# On importe le module routes dans le package app (en non pas
# la variuable). On le place  à la fin pour eviter 
# les import circulaire.