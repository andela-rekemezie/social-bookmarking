from datetime import datetime
from sqlalchemy import desc
from thermos import db


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))

    def __init__(self, url, description, date):
        self.url = url
        self.description = description
        self.date = date

    @staticmethod
    def newest(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)

    def __repr__(self):
        return "<Bookmark '{}': '{}'".format(self.description, self.url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(180), unique=True)
    email = db.Column(db.String(200), unique=True)

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    def __repr__(self):
        return "<User %r>" % self.username