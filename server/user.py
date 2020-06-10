import sqlite3
from flask_restx import Namespace, Resource, reqparse, inputs
api = Namespace('users', description='User resources')

#---------------------------------------------------------------------------
@api.route('/users/<int:user_id>')
@api.param('user_id', description='User ID')
class User(Resource):
    def get(self, user_id):
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute("select name from appuser where id = ?", (user_id,))
        for name, in c:
            return name

