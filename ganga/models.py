# -*- coding: utf-8 -*-

from flask import Flask
from ganga import app, db
from flask.ext.sqlalchemy import SQLAlchemy
from geoalchemy import GeometryColumn, Point


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)

    def init(self, email, password, name, bio=None, photo=None):
        self.email = email
        self.password = password

    def __unicode__(self):
        return u"%s<%s>" % (self.id, self.email)

    @property
    def as_json(self):
        return {'email': self.email, }

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = GeometryColumn(Point(2))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner = db.relationship('User',
                            backref=db.backref('owner', lazy='dynamic'))

    def __init__(self, location, owner_id, name=None,):
        self.location = location
        self.owner_id = owner_id
        self.name = name

    def __unicode__(self):
        return u"Product %s: %s" % (self.pk, self.name,)


if __name__ == "__main__":
    db.create_all()
