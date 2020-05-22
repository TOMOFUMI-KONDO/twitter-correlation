# APIとして利用する機能をまとめたファイル

from flask import Blueprint, jsonify, request, url_for, make_response
from random import *
from flask_cors import CORS

from backend import db
from backend.model import User

api = Blueprint('api', __name__)

@api.route('/hello/')
def hello():
  response = {'msg': 'Hello!'}
  return jsonify(response)

@api.route('/get/')
def getUsers():
  tasks = User.query.order_by(User.id.desc()).all()
  task_list = [task.getUser() for task in tasks]
  return jsonify(task_list)

@api.route('/regist/', methods=['POST'])
def registUser():
  user = User(
    name = request.form['name']
  )
  db.session.add(user)
  db.session.commit()
  user = User.query.order_by(User.id.desc()).first()
  id = str(user.id)
  r = make_response(id)
  return r

@api.route('/delete/', methods=['POST'])
def deleteUser():
  id = request.form['id']
  user = User.query.get(id)
  db.session.delete(user)
  db.session.commit()
  r = make_response(id)
  return r