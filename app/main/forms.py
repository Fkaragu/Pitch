from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')

class PitchForm(FlaskForm):
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    # my_category = StringField('Category', validators=[Required()])
    my_category = SelectField('Category', choices=[('Interview-Pitch','Interview Pitch'),('Product-Pitch','Product Pitch'),('Promotion-Pitch','Promotion Pitch'),('Business','Business'),('Academic','Academic'),('Political','Political'),('Technology','Technology'),('Health','Health')],validators=[Required()])
    submit = SubmitField('Pitch It!')
