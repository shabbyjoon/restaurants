#!/usr/bin/python3

from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast
import sqlite3
from datetime import datetime
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "restaurants.db")


app = Flask(__name__)
api = Api(app)

class Restaurants(Resource):

    def get(self):
        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            con.cursor()
            data = cursor.execute("SELECT * FROM restaurant").fetchall()
            cursor.close()
            curr_time = datetime.now().strftime("%H:%M:%S")

            result = []
            for i in list(data):
                open_time = i[3]
                close_time = i[4]
                open_flag = False

                if open_time <= curr_time and curr_time < close_time:
                    open_flag = True

                rest_info = {'name': i[0], 'open_time': i[3], 'close_time': i[4], 'is_open': open_flag}
                result.append(rest_info)                
                               
            return {'data': result}, 200
  
    def post(self): 
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('address')
        parser.add_argument('phone_number')
        parser.add_argument('opening_time', required=True)
        parser.add_argument('closing_time', required=True)
        parser.add_argument('category')
        parser.add_argument('takeout')
        parser.add_argument('delivery')
        parser.add_argument('menu')
        args = parser.parse_args()
       
        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            con.cursor()
            data = cursor.execute("SELECT * FROM restaurant").fetchall()

            for i in list(data):
                if args['name'] == i[0]:
                    return {
                        'message': f"'{args['name']}' already exists."
                    }, 409

            insert_statement = "INSERT INTO restaurant (name, opening_time, closing_time) VALUES (?, ?, ?)"
            data_tuple = (args['name'], args['opening_time'], args['closing_time'])
                
            cursor.execute(insert_statement, data_tuple)
            con.commit()    
            name = args['name']
            record = cursor.execute("SELECT ROWID, * FROM restaurant WHERE name = ?", (name,)).fetchall()

            cursor.close()
            return {'row_id': record[0][0]}, 201
    pass

api.add_resource(Restaurants, '/restaurants')

if __name__ == '__main__':
    app.run() 