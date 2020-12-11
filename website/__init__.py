from flask import Flask
from configuration.env import Env

app = Flask(__name__)
# Crée une instance de la classe Flask.

app.config.from_object(Env)
# Je defini mon attribut config grace a lacd ap methode from object.
# qui va recupérer la classe de configuration Config

from website import views 
# On importe le module views . On le place  à la fin pour eviter 
# les import circulaire.