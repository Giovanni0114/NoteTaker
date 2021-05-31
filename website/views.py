from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return '<h1>TEST1<h1/>'
