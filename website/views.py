from flask import render_template, flash, redirect, url_for

from grandpy.apiclients.google_places import GooglePlaces
from grandpy.apiclients.google_map import Map
from grandpy.parser.parser import Parser
from website import app 
from website.forms import LoginForm



@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])

def index():
    mape = Map()
    form = LoginForm()
    if form.validate_on_submit():
        parser = Parser(form.question.data)
        flash("Your question : " + form.question.data)
        flash("The parsed string : " + parser.parsed_string)
        google_places_api = GooglePlaces(parser.parsed_string)
        google_places_api.get_places()
        google_places_api.set_attribute()
        flash("GranPy answer : L'adresse de "
                + google_places_api.name
                + " est "
                + google_places_api.address)
        mape.set_place_location(google_places_api.place_id)
        return render_template('index.html', form=form, mape=mape)
    return render_template('index.html', form=form, mape=mape)
