import sqlite3

from flask import jsonify, request
from flask_restx import Namespace, Resource, reqparse, inputs

api = Namespace('users', description='User resources')


# ---------------------------------------------------------------------------
@api.route('/users/<int:user_id>')
@api.param('user_id', description='User ID')
class User(Resource):
    def get(self, user_id):
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute("select name, id from appuser where id = ?", (user_id,))
        for name, id in c:
            return {"id": id, "name": name}


@api.route('/users')
class Users(Resource):
    def get(self):
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute("select name, id from appuser")
        users = []
        for name, id in c:
            users.append({"id": id, "name": name})
        return users

    def post(self):
        data = request.get_json()
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute("select id from appuser order by id desc limit 1")
        id = None
        for ui, in c:
            id = ui+1
        name = data.get('name')
        data["id"] = id
        c.execute("insert into appuser (id, name) values(?,?)", (id, name))
        db.commit()
        return data
