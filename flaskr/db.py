import json


def get_db():
    f = open('flaskr/database/db.json', 'r')
    db = json.loads(f.read())
    return db


def update_db(db):
    sort_db(db)
    f = open('flaskr/database/db.json', 'w')
    json.dump(db, f, indent=4)


def sort_db(db):
    skills = db["skills"]
    skills.sort(key=lambda skill: skill["stars"], reverse=True)
    return db
