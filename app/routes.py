from flask import render_template, flash, redirect, url_for
from app import app #j importe ici app, va variable de classe Flask qui est dans __init__
from app.forms import LoginForm

from app.parser.parser import Parser


@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])
#decorateur qui modifie la fonction route. Ici, si le navigateur demande / ou / index,
#dans tous les cas il retournera le return de la fonvtion index. pkoi index?
# parce que c est la seule view disponible.

def index():
    form = LoginForm()
    if form.validate_on_submit():
        parser = Parser(form.question.data)

        flash(form.question.data)
        flash(parser.parsed_string)

        return redirect(url_for("index")) # cela ramene a index, donc le formulaire sera vié puisque nvelle instance
    return render_template('index.html', form=form)
  