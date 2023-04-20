from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User








@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html' )


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        check_user = User.query.filter_by(username=username ).first()
        if check_user:
            flash('Username already exists', 'danger')
            return redirect(url_for('signup'))
        else:
            new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            flash(f'Guru status achieved {new_user.username}!, dark')
            db.session.add(new_user)
            db.session.commit()
       

      
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
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username or Password is incorrect.', 'danger')
            return redirect(url_for('login'))
        
    return render_template('login.html', form=form)



            

    
    

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'warning')
    return redirect(url_for('index'))






@app.route('/closet', methods=['GET', 'POST'])
def closet():
    return render_template('closet.html')


@app.route('/watchlist', methods=['GET', 'POST'])
def watchlist():
    return render_template('watchlist.html')







