from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, CreateAccountForm, AddNewArtistForm


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
        flash('New Artist Page Created for {}'.format(form.new_artist.data))
        return render_template('artist_page.html', new_artist=form.new_artist.data, town=form.town.data, description=form.description.data)
    return render_template('new_artists.html', title='New Artist', form=form)



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


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash("New User {} Created!".format(form.username.data))
        new_form = CreateAccountForm()
        render_template('create_user.html', title="Create User", form=new_form)

    return render_template('create_user.html', title="Create User", form=form)
