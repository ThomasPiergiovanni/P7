from flask import render_template, flash, redirect, url_for

from grandpy.apiclients.google_map import Map
from grandpy.apiclients.google_places import GooglePlaces
from grandpy.apiclients.mediawiki import MediaWiki
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
        flash("Ma question : " + form.question.data)
        flash("Output parser: " + parser.parsed_string)
        place = GooglePlaces(parser.parsed_string)
        place.get_places()
        place.set_attribute()
        infos = MediaWiki(place.name)
        infos.get_mediawiki()
        infos.set_attribute()
        flash("L'adresse de: "
                + place.name
                + " est "
                + place.address)
        flash("Info wiki: " + infos.information)
        mape.set_place_location(place.place_id)
        return render_template('index.html', form=form, mape=mape)
    return render_template('index.html', form=form, mape=mape)
