from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('content', __name__, url_prefix='/content')


@bp.route('/skills', methods=('GET', 'POST'))
def skills():
    db = get_db()

    skills = db.execute(
        'SELECT ID, NAME, STARS, DESCRIBE, EDIT_TIME'
        ' FROM SKILLS'
        ' ORDER BY STARS DESC'
    ).fetchall()

    return render_template('content/skills.html', skills=skills)


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
            return redirect(url_for('content.skills'))

    return render_template('content/create.html')

