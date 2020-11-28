from flask import render_template, flash, redirect, url_for

from grandpy.apiclients.google_map import Map
from grandpy.apiclients.place import Place
from grandpy.apiclients.mediawiki import MediaWiki
from grandpy.parser.parser import Parser
from website import app 
from website.form import Form


@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])

def index():
    mape = Map()
    form = Form()
    if form.validate_on_submit():
        parser = Parser()
        parser.question = form.question.data
        parser.parse()
        if parser.status:
            flash("Ma question : " + form.question.data)
            flash("Output parser: " + parser.parsed_string)
            place = Place(parser.parsed_string)
            place.get_place()
            place.set_attribute()
            if place.status:
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
            else:
                flash("Mmh je ne comprend pas ce que tu me demandes")
        else:
            flash("Mmh, je n'ai pas compris ce que tu me demandes")
    return render_template('index.html', form=form, mape=mape)
