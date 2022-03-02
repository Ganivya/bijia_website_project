from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('標題', validators=[DataRequired()])
    content = TextAreaField('內容', validators=[DataRequired()])
    submit = SubmitField('發文')