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

class TwitterUser(db.Model):
  __tablename__ = 'twitterUser'
  id = db.Column(db.Integer, primary_key=True)
  twitter_id = db.Column(db.Integer, nullable=False, unique=True, index=True)
  user_name = db.Column(db.String(60))
  # user_image_url = db.Column(db.String(120))

  def __repr__(self):
    return 'TwitterUser: id {0}, twitter_id {1}, user_name {2}'.format(self.id, self.twitter_id, self.user_name)
