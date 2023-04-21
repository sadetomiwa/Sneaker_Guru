from app import app, db, newscatcherapi
from flask import render_template, redirect, url_for, flash, jsonify, request
from app.forms import SignUpForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, Closet
import requests


@app.route('/')
def landing():
    return render_template('landing.html')




@app.route('/home')
def index():
    all_articles = newscatcherapi.get_search(q='Upcoming sneaker releases', lang='en', countries='US', page_size=10)
    articles = all_articles['articles']
    return render_template('home.html', articles=articles)



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
            flash('Guru status achieved !', 'dark')
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







@app.route('/watchlist', methods=['GET', 'POST'])
def watchlist():
    return render_template('watchlist.html')


@app.route('/news')
def get_news():
    
    articles = newscatcherapi.get_top_headlines(lang='en')

    
    results = []
    for article in articles['articles']:
        results.append({
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'image': article['image'] if 'image' in article else None,
            'source': article['source']['name']
        })

   
    return jsonify(results)




@app.route('/search')
def search_shoes():
    query = request.args.get('q', '')
    headers = {
        'X-RapidAPI-Key': app.config['RAPIDAPI_KEY'],
        'X-RapidAPI-Host': 'the-sneaker-database.p.rapidapi.com'
    }
    params = {
        'limit': 10,
        'name': query
    }
    url = "https://the-sneaker-database.p.rapidapi.com/sneakers"
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    results = data['results']
    return render_template('search.html', results=results)





@app.route('/add_to_closet/<sneaker_id>')
@login_required
def add_to_closet(sneaker_id):
    # sneaker_id = request.form.get('sneaker_id')
    if not sneaker_id:
        flash('Error: Sneaker ID not found in request.', 'error')
        return redirect(request.referrer)
    

    
   
    new_closet_item = Closet(user_id=current_user.id, sneaker_id=sneaker_id)
    db.session.add(new_closet_item)
    db.session.commit()



    
    flash('Sneaker added to closet successfully!', 'success')
    return redirect(request.referrer)



@app.route('/closet')
@login_required
def closet():

    closet_items = Closet.query.filter_by(user_id=current_user.id).all()
    

    return render_template('closet.html', closet_items=closet_items)


