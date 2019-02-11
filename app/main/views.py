from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm , PitchFormP, PitchFormI, PitchFormL, CommentForm
from ..models import User, Pitch, Review,Comment, UpVote, DownVote
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

@main.route('/Promotion',methods = ['GET', 'POST'])
@login_required
def Promotion():

    pitch_form = PitchFormP()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        #return redirect(url_for('index.html'))

    all_pitches = Pitch.get_all_pitches()

    title = 'Home | One Minute Pitch'

    return render_template("Promotion.html", pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch(id):

    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)
    # print(all_comments)
    # format_comments = markdown2.markdown(all_comments.comment_content,extras=["code-friendly", "fenced-code-blocks"])

    up_likes = UpVote.get_votes(id)
    down_likes = DownVote.get_downvotes(id)

    title = 'Comment | One Minute Pitch'
    return render_template('pitch.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title, likes = up_likes, dislikes=down_likes)
