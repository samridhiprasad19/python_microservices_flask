#importing all the libraries that are needed
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Column,Integer,String,Float
import os
#providing the name 
app = Flask(__name__)


#configuiring the database ie SQLAlchemy ie where to save the database file the following lines save the code in same root folder
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqllite:///'+os.path.join(basedir,'planets.db')
#defining all the routes needed for application
@app.route('/')
def hello_world():
	return jsonify(message ='Hello World')


@app.route('/not_found')
def not_found():
	return jsonify(message='Page not Found!!'),400


@app.route('/parameters')
def parameters():
	name = request.args.get('name')
	age = int(request.args.get('age'))
	if age < 18:
		return jsonify(message="Sorry!"+name+"You are underage"),401
	else:
			return jsonify(message="Welcome"+name+"You are allowed")


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name:str,age:int):
	if age < 18:
		return jsonify(message="Sorry!"+name+"You are underage"),401
	else:
			return jsonify(message="Welcome"+name+"You are allowed")
	




