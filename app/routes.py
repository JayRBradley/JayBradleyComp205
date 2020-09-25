from flask import render_template
from app import app

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

@app.route('/new_artists')
def new_artists():
    user = {'username': 'Jay'}
    return render_template('new_artists.html', title='New Artist', user=user)

@app.route('/artists')
def artists():
    user = {'username': 'Jay'}
    posts = [
        {
            'post_link': '/artist_page',
            'body': 'Quail'
        },
        {
            'post_link': '',
            'body': 'Vee Da Bee'
        },
        {
            'post_link': '',
            'body': 'Brian!'
        },
        {
            'post_link': '',
            'body': 'Butter'
        }
    ]
    return render_template('artists.html', title='Artists', user=user, posts=posts)

@app.route('/artist_page')
def artist_page():
    user = {'username': 'Jay'}
    return render_template('artist_page.html', title='Artist Page', user=user)


