from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    question = StringField("Questiondd", validators=[DataRequired()])
    submit = SubmitField('Ask')