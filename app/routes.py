from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm


from flask_login import login_user, current_user, logout_user, login_required







@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html' ,loggedin=False)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        flash(f'Guru status achieved {username}!, dark')
        return redirect(url_for('index'))

        
    return render_template('signup.html', form = form)
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Form submitted')
        username = form.username.data
        password = form.password.data
        print(username, password)

        flash(f'Guru status achieved {username}!, dark')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
    
    

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')


@app.route('/closet', methods=['GET', 'POST'])
def closet():
    return render_template('closet.html')


@app.route('/watchlist', methods=['GET', 'POST'])
def watchlist():
    return render_template('watchlist.html')







