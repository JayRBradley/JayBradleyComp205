from datetime import datetime
from app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    artists = db.relationship('Artist', backref='city', lazy='dynamic')
    venues = db.relationship('Venue', backref='city', lazy='dynamic')

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    cityID = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    artistToEvent = db.relationship('ArtistToEvent', backref='artist', lazy='dynamic')


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    cityID = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    events = db.relationship('Event', backref='venue', lazy='dynamic')



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    time = db.Column(db.String(64), index=True)
    venueID = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artistsToEvent = db.relationship('ArtistToEvent', backref='event', lazy='dynamic')



class ArtistToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artistID = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    eventID = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
