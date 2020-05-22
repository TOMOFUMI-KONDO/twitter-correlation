# データベース関連の設定
# SQLAlchemyで扱うモデル(=テーブル)を定義している

from backend import db

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)

  def getUser(self):
    return dict(id=self.id, name=self.name)

def init():
  db.create_all()
