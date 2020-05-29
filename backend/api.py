# APIとして利用する機能をまとめたファイル
from flask import Blueprint, jsonify, request, make_response
import oauth2
import json
import re

from backend import db
from backend.model import User
import backend.config as cf
import backend.TwitterGetter as tg
import backend.SheetGetter as sg
import backend.rank as rank

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

#todo: 本人はランキングに表示されないようにする必要がある
@api.route('/search/', methods=['POST']) # note: GETリクエストにするとパラメータをうまく渡せなかったので、POSTにした。
def search():
  # リクエストで送信されたtwitterのユーザー名から、そのユーザーのツイートに含まれるyoutubeのリンクを取得する
  #======================================================================
  screen_name = request.form['id']
  twitterGetter = tg.TweetGetter(screen_name) # インスタンスを作成

  data = twitterGetter.collect(total=900)

  if 'error' in data:
    return data['error'] # エラーが返ってきたときは呼び出し先にそのエラーをそのまま渡す

  user_movie_urls = data['user_movie_urls']
  print('remark: {}'.format(data['remark']))
  print('{}のツイートから{}件の動画URLを取得'.format(screen_name, len(user_movie_urls)))
  #======================================================================

  #スプレッドシートから比較用のデータを取得する
  #======================================================================
  sheetGetter = sg.SheetGetter()
  users = sheetGetter.getUsers()
  movie_urls = sheetGetter.getMovieUrls()
  watch_list = sheetGetter.getWatchList()
  #======================================================================

  # print(user_movie_urls)
  # print(users)
  # print(movie_urls)
  # print(watch_list)

  rank_data = rank.matome(movie_urls, user_movie_urls, [watch_list[i]['movie'] for i in range(len(watch_list))])
  # print(rank_data)

  ranking = []
  for user in rank_data:
    user_id = users[user[0]]['user_id']
    user_name = users[user[0]]['name']
    icon_url = users[user[0]]['icon_url']

    ranking.append({'user_id': user_id, 'name': user_name, 'icon_url': icon_url})

  return {'ranking': ranking}