# backendディレクトリをパッケージとして初期化

from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask('twitter-correlation', static_folder = './dist/static', template_folder = './dist')
app.config.from_object('backend.config.BaseConfig') # config.pyの設定を取得
db = SQLAlchemy(app)

from backend.api import api
app.register_blueprint(api, url_prefix='/api') # apiを登録
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) # Cross OriginでAPIを叩くことを許可

# Vueでビルドしたindex.htmlにリダイレクト
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  return render_template('index.html')
