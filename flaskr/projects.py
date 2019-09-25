from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db


bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/')
def index():
    return render_template('projects/index.html')