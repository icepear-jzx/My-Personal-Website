from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db, update_db


bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    projects = db["projects"]
    return render_template('projects/index.html', projects=projects)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        describe = request.form['describe']

        db = get_db()
        projects = db["projects"]

        error = None
        for project in projects:
            if project["name"] == name:
                error = "This project already exists."
                break
        
        if error:
            flash(error)
        else:
            new_project = {"name": name, "describe": describe}
            projects.append(new_project)
            update_db(db)  
            return redirect(url_for('projects.index'))

    return render_template('projects/create.html')


@bp.route('/update/<id>', methods=('GET', 'POST'))
def update(id):
    id = int(id)
    db = get_db()
    projects = db["projects"]
    project = projects[id]

    if request.method == 'POST':
        project["name"] = request.form['name']
        project["describe"] = request.form['describe']
        update_db(db)
        return redirect(url_for('projects.index'))

    return render_template('projects/update.html', id=id, project=project)


@bp.route('/delete/<id>', methods=('GET', 'POST'))
def delete(id):
    id = int(id)
    db = get_db()
    projects = db["projects"]
    projects.pop(id)
    update_db(db)
    return redirect(url_for('projects.index'))
