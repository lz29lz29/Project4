import csv
import logging
import os
#import pandas as pd


from flask import Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Transaction
from app.songs.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

songs = Blueprint('songs', __name__,
                        template_folder='templates')

@songs.route('/songs', methods=['GET'], defaults={"page": 1})
@songs.route('/songs/<int:page>', methods=['GET'])
def songs_browse(page):
    page = page
    per_page = 1000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_songs.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)

@songs.route('/songs/upload', methods=['POST', 'GET'])
@login_required
def songs_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")
        log.info("upload the csv file")

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        #data = pd.read_csv(filepath)
        #message = data['AMOUNT'].sum()


        #current_user.balance = current_user.balance + message
        #db.session.add(current_user)
        #db.session.commit()
        balance = current_user.balance
        list_of_transactions = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            list_of_transactions = []
            for row in csv_file:
                list_of_transactions.append(Transaction(row['AMOUNT'], row['TYPE']))
                balance += float(row['AMOUNT'])

        current_user.transactions = list_of_transactions
        current_user.balance = balance
        db.session.commit()

        return redirect(url_for('songs.songs_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)