from flask import render_template, request, jsonify, make_response

from grandpy.apiclients.gmap import Gmap
from grandpy.apiclients.place import Place
from grandpy.apiclients.mediawiki import MediaWiki
from grandpy.parser.parser import Parser
from website import app 
# from website.form import Form


@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])
def index():
    gmap = Gmap()
    return render_template('index.html', gmap=gmap)

@app.route('/index/create-entry', methods=['POST'])
def create_entry():
    demand = request.get_json()

    parser = Parser()
    parser.question = demand["question"]
    parser.parse()
    if parser.status:
        place = Place(parser.parsed_string)
        place.get_place()
        place.set_attribute()
        if place.status:
            mediawiki = MediaWiki(place.name)
            mediawiki.get_mediawiki()
            mediawiki.set_attribute()
            if mediawiki.status:
                gmap = Gmap()
                gmap.set_place_location(place.place_id)

    answer = {
        "parsed_string" : parser.parsed_string,
        "address" : place.address,
        "information" : mediawiki.information,
        "map": gmap.url
    }
    res = make_response(jsonify(answer), 200)
    return res

