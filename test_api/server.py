# The following code comes from here: https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
# The chinook sample database comes from sqlite: http://www.sqlitetutorial.net/sqlite-sample-database/

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

# Practice class 
class Artists(Resource):
    def get(self):
        conn = db_connect.connect() 
        query = conn.execute("select * from artists")
        return {'artists': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        
class Albums(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from albums")
        return {'albums': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    def post(self, artist_id, title):
        conn = db_connect.connect()
        query = conn.execute("insert into albums values (=%d, =%s) " %int(artist_id) %str(title))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Artist(Resource):
    def get(self, artist_id):
        conn = db_connect.connect()
        query = conn.execute("select * from artists where ArtistId =%d "  %int(artist_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Album(Resource):
    def get(self, album_id):
        conn = db_connect.connect()
        query = conn.execute("select * from albums where AlbumId =%d "  %int(album_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(Artists, '/artists')
api.add_resource(Albums, '/albums')
api.add_resource(Artist, '/artists/<artist_id>')
api.add_resource(Album, '/albums/<album_id>')


if __name__ == '__main__':
     app.run(port=5002)