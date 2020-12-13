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
    """Index view
    """
    gmap = Gmap()
    gmap.set_default_location()
    return render_template('index.html', gmap=gmap)


@app.route('/index/create-entry', methods=['POST'])
def create_entry():
    """View when question is submitted
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
    mediawiki.set_attribute()
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
        "map": gmap.url
    }
    response = make_response(jsonify(answer), 200)
    return response
