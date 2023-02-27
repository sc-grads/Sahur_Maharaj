from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/thankyou', methods=['POST'])
def thank_you():
    first = request.form['first']
    return render_template('thankyou.html', first=first)


@app.route('/index_')
def index_():
    uName = 'Shay'
    list_user = list('abcde')
    return render_template('Default.html', uName=uName, list_user=list_user)


@app.route('/puppy_latin/<pup_name>')
def puppy_latin(pup_name):
    pup_name = pup_name.lower()
    if pup_name[-1] != 'y':
        pup_name = pup_name + 'y'
        return pup_name
    else:
        pup_name = pup_name[:-1] + 'iful'
        return pup_name


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/about/<name>')
def other_about(name):
    return f'user is {name.upper()}'


if __name__ == '__main__':
    print(app.config)
    app.run(debug=True)
