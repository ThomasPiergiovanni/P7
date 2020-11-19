from flask import Flask
from configuration.config import Config

app = Flask(__name__) # Crée une instance de la classe Flask.
app.config.from_object(Config)


from app import routes # On importe le module routes dans le package app (en non pas la variuable)
                        # On le place  à la fin pour eviter les import circulaire.