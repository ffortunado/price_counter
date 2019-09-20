from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '123'}
    return render_template('index.html', title='title', user=user)
