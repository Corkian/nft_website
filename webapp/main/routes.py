from flask import render_template, request, Blueprint
from .utility import sendContactForm
from webapp import db
from webapp.db_models import Subscriber
from webapp.config import Config

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        result = {}
        result['name'] = request.form['name']
        result['email'] = request.form['email'].replace(' ', '').lower()
        result['message'] = request.form['message']

        response = sendContactForm(result)

        return render_template('contact.html', response=response)

    return render_template('contact.html')


@main_bp.route("/subscribe", methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        result = request.form['emailsub'].replace(' ', '').lower()
        if result:
            new_subscriber = Subscriber(email=result)
            db.session.add(new_subscriber)
            db.session.commit()

        return render_template('index.html', result=result)
