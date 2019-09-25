from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('skills', __name__, url_prefix='/skills')


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()

    skills = db.execute(
        "SELECT ID, NAME, STARS, DESCRIBE, EDIT_TIME"
        " FROM SKILLS"
        " ORDER BY STARS DESC"
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
                "INSERT INTO SKILLS (NAME, STARS, DESCRIBE)"
                " VALUES (?, ?, ?)",
                (name, stars, describe)
            )
            db.commit()
            return redirect(url_for('skills.index'))

    return render_template('skills/create.html')


@bp.route('/update/<skill>', methods=('GET', 'POST'))
def update(skill):
    db = get_db()

    skill = db.execute(
        "SELECT ID, NAME, STARS, DESCRIBE, EDIT_TIME"
        " FROM SKILLS"
        " WHERE NAME == '{}'".format(skill)
    ).fetchone()

    id = skill['ID']

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
                "UPDATE SKILLS"
                " SET NAME = '{}', STARS = '{}', DESCRIBE = '{}'"
                " WHERE ID == '{}'".format(name, stars, describe, id)
            )
            db.commit()
            return redirect(url_for('skills.index'))

    return render_template('skills/update.html', skill=skill)


@bp.route('/delete/<skill>', methods=('GET', 'POST'))
def delete(skill):
    db = get_db()
    db.execute(
        "DELETE FROM SKILLS"
        " WHERE NAME == '{}'".format(skill)
    )
    db.commit()
    return redirect(url_for('skills.index'))
