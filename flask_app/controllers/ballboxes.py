from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models.user import User
from flask_app.models.ballbox import Ballbox

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def login_and_registration():
    return render_template('BallBox.html')

@app.route('/registration', methods=['POST'])
def registration():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']
    }

    if User.validate_registration(data):
        data['password'] = bcrypt.generate_password_hash(data['password'])
        user_id = User.create_user(data)
        session["user_id"] = user_id
        return redirect('/dashboard')
    
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    users = User.get_all_users()

    all_users = []

    for user in users:
        data = {
            'user_id': user['id']
        }

        all_users.append(User.get_user_by_id(data))
        
    return render_template('Dashboard.html', all_users = all_users)

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }

    if User.validate_login(data, bcrypt):
        user = User.get_user_by_email(data)
        session['user_id'] = user.id

        return redirect('/dashboard')
    
    return redirect('/')

@app.route('/logout')
def logout_user():
    session.clear()

    return redirect('/')

@app.route('/new')
def create_ballbox():
    if 'user_id' not in session:
        return redirect('/')
        
    return render_template('CreateBox.html')

@app.route('/add/new', methods=['POST'])
def add_ballbox():

    data = {
        'title': request.form['title'],
        'box_height': request.form['box_height'],
        'box_width': request.form['box_width'],
        'box_background_color': request.form['box_background_color'],
        'box_gradient': request.form['box_gradient'],
        'box_border_width': request.form['box_border_width'],
        'box_radius': request.form['box_radius'],
        'box_border_color': request.form['box_border_color'],
        'ball_amount': request.form['ball_amount'],
        'ball_size': request.form['ball_size'],
        'ball_background_color': request.form['ball_background_color'],
        'ball_gradient': request.form['ball_gradient'],
        'ball_border_width': request.form['ball_border_width'],
        'ball_border_color': request.form['ball_border_color'],
        'user_id': session['user_id']
    }

    Ballbox.create_ballbox(data)
    
    return redirect('/dashboard')

@app.route('/show/<int:ballbox_id>')
def show_magazine(ballbox_id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'box_id': ballbox_id
    }

    ballbox = Ballbox.get_ballbox_by_id(data)

    return render_template('Box.html', ballbox = ballbox)