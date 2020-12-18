"""Views module
"""
from flask import render_template, request, jsonify, make_response

from grandpy.apiclients.gmap import Gmap
from grandpy.apiclients.place import Place
from grandpy.apiclients.mediawiki import MediaWiki
from grandpy.parser.parser import Parser
from website import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Route of index page i.e. the main page.
    """
    return render_template('index.html')


@app.route('/index/get-url', methods=['GET'])
def get_url():
    """Route when arriving on index page. It get map url back.
    """
    gmap = Gmap()
    gmap.set_default_location()
    answer = {
            "gmap_url": gmap.gmap_url
    }
    response = make_response(jsonify(answer), 200)
    return response


@app.route('/index/create-entry', methods=['POST'])
def create_entry():
    """Route when question is submitted. It gets Google Place and Map API and
    WikiMedia informations back.
    """
    demand = request.get_json()
    parser = Parser()
    parser.question = demand["question"]
    parser.parse()
    place = Place(parser.parsed_chain)
    place.get_place()
    place.set_attribute()
    mediawiki = MediaWiki(place.name)
    mediawiki.get_mediawiki()
    mediawiki.set_attribute(place.name)
    if place.status:
        gmap = Gmap()
        gmap.set_place_location(place.place_id)
    else:
        gmap = Gmap()
        gmap.set_default_location()
    answer = {
            "parser_status": parser.status,
            "parsed_chain": parser.parsed_chain,
            "address_status": place.status,
            "address": place.address,
            "information_status": mediawiki.status,
            "information": mediawiki.information,
            "wikipedia_url": mediawiki.wikipedia_url,
            "gmap_url": gmap.gmap_url
    }
    response = make_response(jsonify(answer), 200)
    return response
