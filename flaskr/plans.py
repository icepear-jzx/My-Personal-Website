from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db


bp = Blueprint('plans', __name__, url_prefix='/plans')


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()

    plans = db.execute(
        "SELECT ID, NAME, TIMESPAN, START_TIME, END_TIME, FINISHED, GOAL"
        " FROM PLANS"
        " ORDER BY GOAL DESC"
    ).fetchall()

    return render_template('plans/index.html', plans=plans)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['NAME']
        timespan = request.form['TIMESPAN']
        start_time = request.form['START_TIME']
        end_time = request.form['END_TIME']
        finished = request.form['FINISHED']
        goal = request.form['GOAL']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO PLANS (NAME, TIMESPAN, START_TIME, END_TIME, FINISHED, GOAL)"
                " VALUES (?, ?, ?, ?, ?, ?)",
                (name, timespan, start_time, end_time, finished, goal)
            )
            db.commit()
            return redirect(url_for('plans.index'))

    return render_template('plans/create.html')


@bp.route('/update/<plan>', methods=('GET', 'POST'))
def update(plan):
    db = get_db()

    plan = db.execute(
        "SELECT ID, NAME, TIMESPAN, START_TIME, END_TIME, FINISHED, GOAL"
        " FROM PLANS"
        " WHERE NAME == '{}'".format(plan)
    ).fetchone()

    id = plan['ID']

    if request.method == 'POST':
        name = request.form['NAME']
        timespan = request.form['TIMESPAN']
        start_time = request.form['START_TIME']
        end_time = request.form['END_TIME']
        finished = request.form['FINISHED']
        goal = request.form['GOAL']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE PLANS"
                " SET NAME = '{}', TIMESPAN = '{}', START_TIME = '{}',"
                " END_TIME = '{}', FINISHED = '{}', GOAL = '{}'"
                " WHERE ID == '{}'".format(name, timespan, start_time, end_time, finished, goal, id)
            )
            db.commit()
            return redirect(url_for('plans.index'))

    return render_template('plans/update.html', plan=plan)


@bp.route('/delete/<plan>', methods=('GET', 'POST'))
def delete(plan):
    db = get_db()
    db.execute(
        "DELETE FROM PLANS"
        " WHERE NAME == '{}'".format(plan)
    )
    db.commit()
    return redirect(url_for('plans.index'))
