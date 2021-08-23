from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sidharth'}
    posts = [
        {
            'author': {'username': 'Avinash'},
            'body': 'Beautiful day!'
        },
        {
            'author': {'username': 'Trisha'},
            'body': 'Practical Python is awesome!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
