from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField , DateField
from wtforms.validators import DataRequired, EqualTo , length


class PatientForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    uniqe_id = IntegerField('uniqe_id', validators=[DataRequired() ])
    birth_day = DateField('birth_day', validators=[DataRequired()])
    submit = SubmitField('submit')

class Search(FlaskForm):
    uniqe_id = StringField('uniqe_id' , validators=[DataRequired() , length(max=30)] )
    submit = SubmitField('submit')
    
