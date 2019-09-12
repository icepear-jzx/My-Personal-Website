from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('skills', __name__, url_prefix='/skills')


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()

    skills = db.execute(
        'SELECT ID, NAME, STARS, DESCRIBE, EDIT_TIME'
        ' FROM SKILLS'
        ' ORDER BY STARS DESC'
    ).fetchall()

    return render_template('skills/index.html', skills=skills)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['NAME']
        stars = request.form['STARS']
        describe = request.form['DESCRIBE']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO SKILLS (NAME, STARS, DESCRIBE)'
                ' VALUES (?, ?, ?)',
                (name, stars, describe)
            )
            db.commit()
            return redirect(url_for('skills.index'))

    return render_template('skills/create.html')

