from app import app
from flask import render_template
from app.forms import SignUpForm, LoginForm

from flask_login import login_user, current_user, logout_user, login_required







@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return render_template('signup.html', form=form)
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('login.html', form=form)
    
    

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')



