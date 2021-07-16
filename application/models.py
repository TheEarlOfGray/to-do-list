from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(50), default=" ")#
    comp = db.Column(db.Boolean, default=False)

class AddForm(FlaskForm):
    name = StringField('Name')
    desc = StringField('Description')
    comp = BooleanField('Completed')
    submit = SubmitField('Add Task')
