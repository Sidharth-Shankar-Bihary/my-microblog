from app import app
from flask import render_template


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
