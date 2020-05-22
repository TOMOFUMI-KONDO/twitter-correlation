# バックエンドの設定ファイル
# 環境変数を定義したりする
import os

class BaseConfig(object):
  DEBUG = True # 開発モード

  SQLALCHEMY_DATABASE_URI = 'sqlite:///backend.db'
  SECRET_KEY = os.urandom(24)
