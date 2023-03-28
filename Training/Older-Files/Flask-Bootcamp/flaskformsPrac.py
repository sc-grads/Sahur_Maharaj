from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                     DateTimeField, RadioField, SelectField, TextAreaField)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'DONTPUTTHISHERE'
class info_form(FlaskForm):
    breed = StringField("What Breed are you ")
    submit = SubmitField("Submit")
        
    
@app.route('/', methods=['GET', 'POST'])    
def frm_new():
    breed = False
    form = info_form()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''
    return render_template('home.html', form=form, breed=breed)
    
    
if __name__ == '__main__':
    app.run(debug=True)