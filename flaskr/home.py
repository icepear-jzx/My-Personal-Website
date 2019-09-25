from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db


bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def index():
    return render_template('home/index.html')

