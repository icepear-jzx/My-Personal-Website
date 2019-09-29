from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db, update_db

import random, copy

bp = Blueprint('skills', __name__, url_prefix='/skills')


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    skills = db["skills"]
    skills_disorder = copy.deepcopy(skills)
    random.shuffle(skills_disorder)
    return render_template('skills/index.html', skills=skills, skills_disorder=skills_disorder)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        stars = int(request.form['stars'])
        describe = request.form['describe']

        db = get_db()
        skills = db["skills"]

        error = None
        for skill in skills:
            if skill["name"] == name:
                error = "This skill already exists."
                break
        
        if error:
            flash(error)
        else:
            new_skill = {"name": name, "stars": stars, "describe": describe}
            skills.append(new_skill)
            update_db(db)  
            return redirect(url_for('skills.index'))

    return render_template('skills/create.html')


@bp.route('/update/<id>', methods=('GET', 'POST'))
def update(id):
    id = int(id)
    db = get_db()
    skills = db["skills"]
    skill = skills[id]

    if request.method == 'POST':
        skill["stars"] = int(request.form['stars'])
        skill["describe"] = request.form['describe']
        update_db(db)
        return redirect(url_for('skills.index'))

    return render_template('skills/update.html', id=id, skill=skill)


@bp.route('/delete/<id>', methods=('GET', 'POST'))
def delete(id):
    id = int(id)
    db = get_db()
    skills = db["skills"]
    skills.pop(id)
    update_db(db)
    return redirect(url_for('skills.index'))
