from flask import render_template, flash, redirect, url_for

from grandpy.apiclients.google_places import GooglePlaces
from grandpy.parser.parser import Parser
from website import app #j importe ici app, va variable de classe Flask qui est dans __init__
from website.forms import LoginForm




@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])
#decorateur qui modifie la fonction route. Ici, si le navigateur demande / ou / index,
#dans tous les cas il retournera le return de la fonvtion index. pkoi index?
# parce que c est la seule view disponible.

def index():
    form = LoginForm()
    if form.validate_on_submit():
        parser = Parser(form.question.data)
        flash("Your question : " + form.question.data)
        flash("The parsed string : " + parser.parsed_string)
        google_places_api = GooglePlaces(parser.parsed_string)
        google_places_api.get_places()
        google_places_api.get_attribute()
        flash("GranPy answer : " + google_places_api.address)



        return redirect(url_for("index")) # cela ramene a index, donc le formulaire sera vié puisque nvelle instance
    return render_template('index.html', form=form)
