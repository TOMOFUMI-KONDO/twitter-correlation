# twitter-correlation

## 構成
- backend (python)
- requirements.txt (pipのパッケージ一覧)
- frontend (Vue)
- dist (Vueの出力先)
- manage.py (これを実行してサーバー立てる)

## 最初にすること
- ルート直下で "pip install -r requirements.txt" (pipのパッケージがインストールされる)
- frontend直下で "npm install" (npmのパッケージがインストールされる)

## その他使うコマンド
- ルート直下で "python manage.py" (バックエンドのコード書くとき、ローカルサーバー立てる)
- frontend直下で "npm run serve" (フロントエンドのコード書くとき、ローカルサーバー立てる)
- frontend直下で "npm run lint" (コードをきれいに直してくれる。複数人で開発してもコードの美しさを保つため。)
- frontend直下で "npm run build" (ルート直下のdistファイルにbuildする。バックエンドのサーバーはこのdist配下のファイルを使うため、pythonで立てたサーバーから見たフロントエンドのコードを更新する時はbuildする必要がある。)