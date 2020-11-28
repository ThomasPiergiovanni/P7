from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    submit = SubmitField('Ask')
