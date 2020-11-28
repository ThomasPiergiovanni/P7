from flask import render_template, flash, redirect, url_for

from grandpy.apiclients.gmap import Gmap
from grandpy.apiclients.place import Place
from grandpy.apiclients.mediawiki import MediaWiki
from grandpy.parser.parser import Parser
from website import app 
from website.form import Form


@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])

def index():
    gmap = Gmap()
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
                mediawiki = MediaWiki(place.name)
                mediawiki.get_mediawiki()
                mediawiki.set_attribute()
                if mediawiki.status:
                    flash("L'adresse de: "
                            + place.name
                            + " est "
                            + place.address)
                    flash("Info wiki: " + mediawiki.information)
                    gmap.set_place_location(place.place_id)
                    return render_template('index.html', form=form, gmap=gmap)
                else:
                    flash("Mmh, pas d'info sur ce lieu")
            else:
                flash("Mmh, je ne connais pas cet endroit")
        else:
            flash("Mmh, je n'ai pas compris ce que tu me demandes")
    return render_template('index.html', form=form, gmap=gmap)
