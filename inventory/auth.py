from flask import Blueprint, render_template, request, redirect, url_for, session, flash,g
from functools import wraps
from inventory.db import mongo
from werkzeug.security import generate_password_hash, check_password_hash
#no sufix currently
auth = Blueprint('auth', __name__)

@auth.before_app_request
def beforeLogin():
    userid=session.get('user_id');

    if userid is None:
        g.user=None
    else:
        g.user=mongo.db.users.find_one({'_id':userid})

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            error="Invalid username or password please try again later"

    return render_template('login.html',error=error)

@auth.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        mongo.db.users.insert_one({'username': username, 'password': hashed_password})
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
