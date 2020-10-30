from datetime import datetime
from app import db
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, CreateAccountForm, AddNewArtistForm
from app.models import ArtistToEvent, Artist, Venue, Event, City


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jay'}
    posts = [
        {
            'author': {'username': 'Quail'},
            'body': 'New Music Soon!'
        }]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/new_artists', methods=('GET', 'POST'))
def new_artists():
    form = AddNewArtistForm()

    if form.validate_on_submit():
        new_artist = form.new_artist.data
        if Artist.query.filter_by(name=new_artist).first() is not None:
            flash('Artist Already Exists')
            return redirect('artists/' + new_artist)
        flash('New Artist Page Created for {}'.format(form.new_artist.data))

        c1 = City(name=form.town.data)
        db.session.add(c1)
        db.session.commit()
        a1 = Artist(name=new_artist, description=form.description.data, cityID=c1.id)
        db.session.add(a1)
        db.session.commit()
        return redirect('artists/' + new_artist)

    return render_template('new_artists.html', title='New Artist', form=form)


@app.route('/artists')
def artists():
    #artist = Artist.query.filter_by(StageName=form.ArtistName.data).first_or_404()
    artists = Artist.query.all()
    return render_template('artists.html', title='Artists', artists=artists)


@app.route('/artist_page')
def artist_page():
    user = {'username': 'Jay'}
    return render_template('artist_page.html', title='Artist Page', user=user)


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash("New User {} Created!".format(form.username.data))
        new_form = CreateAccountForm()
        render_template('create_user.html', title="Create User", form=new_form)

    return render_template('create_user.html', title="Create User", form=form)


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()
    return render_template('base.html', title='DB Reset')


@app.route('/artists/<name>')
def artist(name):
    artist = Artist.query.filter_by(name=name).first()
    events = Event.query.join(Event.artistsToEvent).filter_by(artistID=artist.id)

    return render_template('artist_page.html', title='Artist Page', artist=artist, events=events)




@app.route('/populate_db')
def populate_db():
    c1 = City(name='Ithaca, NY')
    c2 = City(name='Binghamton, NY')
    c3 = City(name='Syracuse, NY')
    c4 = City(name='Rochester, NY')
    db.session.add_all([c1, c2, c3, c4])
    db.session.commit()
    a1 = Artist(name="Driftwood", description="Folk Rock", cityID=c2.id)
    a2 = Artist(name="Quail", description="Funk and Brass", cityID=c1.id)
    a3 = Artist(name="VeeDaBee", description="Rock Band", cityID=c1.id)
    a4 = Artist(name="Danielle Ponder", description="Soul", cityID=c4.id)
    db.session.add_all([a1, a2, a3, a4])
    db.session.commit()
    v1 = Venue(name='The Haunt', cityID=c2.id)
    v2 = Venue(name='State Theater', cityID=c1.id)
    v3 = Venue(name='Stewart Park', cityID=c1.id)
    v4 = Venue(name='University', cityID=c2.id)
    v5 = Venue(name='Oncenter', cityID=c3.id)
    db.session.add_all([v1, v2, v3, v4, v5])
    db.session.commit()
    e1 = Event(name='Ithaca Porchfest', time='11-05-20', venueID=v3.id)
    e2 = Event(name='2020 Tour', time=('10-20-20'), venueID=v5.id)
    e3 = Event(name='Anniversary Concert', time=('10-20-20'), venueID=v1.id)
    e4 = Event(name='2020 Tour', time='10-29-20', venueID=v2.id)
    e5 = Event(name='2020 Tour', time=('12-20-20'), venueID=v4.id)
    db.session.add_all([e1, e2, e3, e4, e5])
    db.session.commit()
    x1 = ArtistToEvent(artistID=a1.id, eventID=e3.id)
    x2 = ArtistToEvent(artistID=a2.id, eventID=e3.id)
    x3 = ArtistToEvent(artistID=a1.id, eventID=e1.id)
    x4 = ArtistToEvent(artistID=a3.id, eventID=e4.id)
    x5 = ArtistToEvent(artistID=a4.id, eventID=e5.id)
    x6 = ArtistToEvent(artistID=a3.id, eventID=e2.id)
    db.session.add_all([x1, x2, x3, x4, x5, x6])
    db.session.commit()

    return render_template('base.html', title='Populate DB')
