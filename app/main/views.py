from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm
from ..models import Review
from flask_login import login_required, current_user

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    #popular_movies = get_movies('popular')
    #upcoming_movie = get_movies('upcoming')
    #now_showing_movie = get_movies('now_playing')

    title = 'Welcome to the One Minute Pitch'

    return render_template("index.html", title=title)

@main.route('/Interview')
@login_required
def Interview():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template("Interview.html")

@main.route('/Pickupline')
@login_required
def Pickupline():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template("Pickupline.html")

@main.route('/Promotion')
@login_required
def Promotion():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template("Promotion.html")
