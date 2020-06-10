import sqlite3
from flask_restx import Namespace, Resource, reqparse, inputs
api = Namespace('users', description='User resources')

#---------------------------------------------------------------------------
@api.route('/users')
class User(Resource):
    def get(self):
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute("select * from appuser")
        for name, , id, in c:
            return {"id" : id, "name" : name}

