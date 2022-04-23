from flask import Blueprint, render_template, url_for







auth = Blueprint('auth', __name__, template_folder='templates', url_prefix= '/auth')

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


