from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                     DateTimeField, RadioField, SelectField, TextAreaField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'DONTPUTTHISHERE'


class Info(FlaskForm):
    u_name = StringField('Enter your name: ', validators=[DataRequired()])
    checked_in = BooleanField('Checking in? ', validators=[DataRequired()])
    activity = RadioField('What are you doing', choices=[
                          ('meeting_id', 'Meeting'), ('training_id', 'Training')])
    date_today = SelectField(u'What day is today: ', choices=[
                             ('day_1', 'Monday'), ('day_2', 'Tuesday')])
    notes = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def typefrm():
    form = Info()
    if form.validate_on_submit():
        session['user'] = form.u_name.data
        session['check'] = form.checked_in.data
        session['activity'] = form.activity.data
        session['today_date'] = form.date_today.data
        session['note'] = form.notes.data
        flash('Button has been clicked')

        return redirect(url_for('thankyouusr'))
    return render_template('ureg.html', form=form)


@app.route('/thankyouusr')
def thankyouusr():
    return render_template('thankyouusr.html')


if __name__ == '__main__':
    app.run(debug=True)
