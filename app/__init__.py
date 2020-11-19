from flask import Flask

grandpy = Flask(__name__) # Crée une instance de la classe Flask. 

from grandpy import routes # On importe le module routes dans le package app (en non pas la variuable)
                        # On le place  à la fin pour eviter les import circulaire.