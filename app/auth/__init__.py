from flask import Blueprint, render_template, url_for







auth = Blueprint('auth', __name__, template_folder='templates', url_prefix= '/auth')

@auth.route('/login')
def login():
    return render_template('login.html')





