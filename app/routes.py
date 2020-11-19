from flask import render_template
from app import app #j importe ici app, va variable de classe Flask qui est dans __init__

@app.route('/') 
@app.route('/index')
#decorateur qui modifie la fonction route. Ici, si le navigateur demande / ou / index,
#dans tous les cas il retournera le return de la fonvtion index. pkoi index?
# parce que c est la seule view disponible.

def index():
    return render_template("index.html")
    