# バックエンドの設定ファイル
# 環境変数を定義したりする
import os
from dotenv import load_dotenv

class BaseConfig(object):
  DEBUG = True # 開発モード

  SQLALCHEMY_DATABASE_URI = 'sqlite:///backend.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.urandom(24)

load_dotenv()
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
TOKEN_KEY = os.environ['TOKEN_KEY']
TOKEN_SECRET = os.environ['TOKEN_SECRET']

SPREADSHEET_KEY = os.environ['SPREADSHEET_KEY']