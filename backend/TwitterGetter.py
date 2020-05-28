import oauth2
import json
import re

import backend.config as cf


class TweetGetter(object):
  def __init__(self, screen_name):
    consumer = oauth2.Consumer(key=cf.API_KEY, secret=cf.API_SECRET)
    token = oauth2.Token(key=cf.TOKEN_KEY, secret = cf.TOKEN_SECRET)
    self.client = oauth2.Client(consumer, token)
    self.screen_name = screen_name
    self.max_id = None
    self.headers = {"content-type": "application/json"}
    self.no_tweet_count = 0

  # ツイートからyoutubeのリンクを抜き出してlistにする
  def collect(self, total=-1):
    isRemain = self.checkLimit()
    if not isRemain:
      return {'error': 'Not Remain'}

    user_movie_urls = []

    while True:
      url = self.createUrl()
      header, content = self.client.request(url, method='GET', body="".encode('utf-8'), headers=self.headers)

      tweets = self.pickUpTweet(content)
      if len(tweets) == 0:
        self.no_tweet_count += 1
      else:
        self.no_tweet_count = 0

      if self.no_tweet_count > 5: #6回以上取得ツイートが0だったら処理を終了
        if len(user_movie_urls) == 0:
          return {'error': 'Get No Tweet'}
        else:
          return {'user_movie_urls': user_movie_urls, 'remark': 'Finish by Get No Tweet'}

      for tweet in tweets:
        urls = tweet['entities']['urls']
        if len(urls) > 0:
          for url in urls:
            expanded_url = url['expanded_url']
            if re.search('youtu.be|youtube.com', expanded_url): # 正規表現で指定した文字列が含まれるか判定
              user_movie_urls.append(expanded_url)

      self.max_id = tweet['id'] - 1

      if len(user_movie_urls) >= total:
        return {'user_movie_urls': user_movie_urls, 'remark': 'Finish by Get Total'}

      if 'X-Rate-Limit-Remaining' in header:
        if int(header['X-Rate-Limit-Remaining']) == 0:
          if len(user_movie_urls) == 0:
            return {'error': 'Not Remain'}
          else:
            return {'user_movie_urls': user_movie_urls, 'remark': 'Finish by Not Remain'}

  # APIの取得制限をチェックする
  def checkLimit(self):
    url = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
    header, content = self.client.request(url, method='GET', body="".encode('utf-8'), headers=self.headers)

    json_data = content.decode('utf8')
    try:
      data = json.loads(json_data) # dataにはdict型が入る
    except ValueError as e: # json.loadsが失敗した時は空のlistを返す
      return []

    remaining = data['resources']['statuses']['/statuses/user_timeline']['remaining']
    print('remaining: {}'.format(remaining))

    return int(remaining) > 0 #取得可能回数が1以上ならTrueを返す

  # twitter apiにリクエストする際のURLとパラメータを設定
  def createUrl(self):
    params = {
      'screen_name': self.screen_name,
      'count': '900',
      'max_id': self.max_id
    }

    for param in params:
      value = params[param]
      if param == 'screen_name':
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json' + '?screen_name=' + value
      elif param == 'max_id':
        if value != None:
          url = url + '&max_id=' + str(value)
      else:
        url = url + '&' + param + '=' + value

    return url

  # APIで取得したツイート情報を整形する
  def pickUpTweet(self, res):
    json_data = res.decode('utf8')
    try:
      data = json.loads(json_data) # dataにはdict型のlistが入る
    except ValueError as e: # json.loadsが失敗した時は空のlistを返す
      return []

    return data
