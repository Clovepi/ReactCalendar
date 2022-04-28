from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS 
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Month(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    start_day = db.Column(db.Integer, nullable=False)
    days_in_month = db.Column(db.Integer, nullable=False)
    past_days = db.Column(db.Integer, nullable=False)
    reminders = db.Column(db.relationship('Reminder', backref='month', cascade='all, delete, delete-orphan'))

    def __init__(self, name, year, start_day, days_in_month, past_days,)
        self.name = name
        self.year - year
        self.start_day = start_day
        self.days_in_month = days_in_month
        self.past_days = past_days

class Reminder(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    month_id = db.Column(db.Integer, db.ForeignKey('month.id'), nullable=False)

    def __init__(self, text, date, month_id):
        self.text = text
        self.date = date
        self.month_id = month_id

class ReminderSchema(ma.Schema):
    class Meta:
        fields = ("id", "text", "date", "month_id")

reminder_schema = ReminderSchema()
multiple_reminder_schema = ReminderSchema(many=True)

class MonthSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "year", "start_day", "days_in_month", "past_days", "reminders")
    reminders = ma.Nested(multiple_reminder_schema)

month_schema = MonthSchema()
multiple_month_schema = MonthSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)