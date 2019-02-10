from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm
from ..models import Review
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = 'Welcome to the One Minute Pitch'

    return render_template("index.html", title=title)

@main.route('/user/<uname>&<id_user>')
@login_required
def profile(uname, id_user):

    user = User.query.filter_by(username = uname).first()
    title = f"{uname.capitalize()}'s Profile"

    get_pitches = Pitch.query.filter_by(user_id = id_user).all()
    get_comments = Comment.query.filter_by(user_id = id_user).all()
    get_upvotes = UpVote.query.filter_by(id_user = id_user).all()
    get_downvotes = DownVote.query.filter_by(id_user = id_user).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user, title=title, pitches_no = get_pitches, comments_no = get_comments, likes_no = get_upvotes, dislikes_no = get_downvotes)
