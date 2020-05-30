import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import backend.config as cf

class SheetGetter(object):
  def __init__(self):
    #APIを認証
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('twitube-b6ed56106252.json', scope)
    self.gc = gspread.authorize(credentials)
    self.url_len = 0

  #ユーザー一覧を返す
  def getUsers(self):
    workbook = self.gc.open_by_key(cf.SPREADSHEET_KEY)

    user_sheet = workbook.worksheet('Userテーブル')
    user_id = user_sheet.col_values(1)[1:]
    name = user_sheet.col_values(2)[1:]
    icon_url = user_sheet.col_values(3)[1:]

    length = len(user_id)
    users = []
    for i in range(length):
      users.append({'user_id': user_id[i], 'name': name[i], 'icon_url': icon_url[i]})

    users.sort(key=lambda x: x['user_id'])

    return users

  #動画のURL一覧を返す
  def getMovieUrls(self):
    workbook = self.gc.open_by_key(cf.SPREADSHEET_KEY)

    movie_sheet = workbook.worksheet('Movieテーブル')
    urls = movie_sheet.col_values(2)[1:]
    self.url_len = len(urls) #getWatchListで使う

    return urls

  #ユーザーごとに任意の動画を見たかどうかの一覧を返す
  def getWatchList(self):
    workbook = self.gc.open_by_key(cf.SPREADSHEET_KEY)

    tweet_sheet = workbook.worksheet('Tweetテーブル')
    movie_id = tweet_sheet.col_values(1)[1:]
    user_id = tweet_sheet.col_values(2)[1:]

    if len(movie_id) >= len(user_id):
      length = len(user_id)
    else:
      length = len(movie_id)
      
    tweets = []
    for i in range(length):
      tweets.append({'movie_id': movie_id[i], 'user_id': user_id[i]})

    tweets.sort(key=lambda x: x['user_id']) #user_idで並び替え

    #1つのuser_idと複数のmovie_url(list)を持つ辞書型のlistにする
    tmp_user_id = tweets[0]['user_id']
    user_num = 0
    watch_list = [{'user_id': tmp_user_id, 'movie_id': [tweets[0]['movie_id']]}]
    for j in range(length-1):
      i = j + 1
      if tweets[i]['user_id'] == tmp_user_id:
        watch_list[user_num]['movie_id'].append(tweets[i]['movie_id'])
      else:
        user_num += 1
        tmp_user_id = tweets[i]['user_id']
        watch_list.append({'user_id': tmp_user_id, 'movie_id': [tweets[i]['movie_id']]})

    #ユーザーごとに任意の動画を見たかどうかを01で示す配列を作成する
    new_watch_list = [{'user_id': watch_list[i]['user_id'], 'movie': []} for i in range(len(watch_list))]
    for i in range(self.url_len): #動画の数だけ回す
      for j in range(len(watch_list)): #ユーザー数だけ回す
        if str(i+1) in watch_list[j]['movie_id']:
          new_watch_list[j]['movie'].append(1)
        else:
          new_watch_list[j]['movie'].append(0)

    return new_watch_list
