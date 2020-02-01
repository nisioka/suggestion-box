import os
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db.sqlite3'),
    SECRET_KEY='hoge',
))


# 以下、DB接続関連の関数


# 以下、画面/機能毎の関数

@app.route('/')
def index():
    """ 一覧画面 """
    return render_template('index.html', results={})


@app.route('/ja')
def index_ja():
    """ 一覧画面 """
    return render_template('index_ja.html', results={})


@app.route('/create', methods=['GET'])
def edit():
    """ 新規作成画面 """
    return render_template('create.html')


@app.route('/ja/create', methods=['GET'])
def edit_ja():
    """ 新規作成画面 """
    return render_template('create_ja.html')


@app.route('/create', methods=['POST'])
def create():
    """ 新規作成処理 """
    return redirect(url_for('view', pk=0))


@app.route('/create', methods=['POST'])
def create_ja():
    """ 新規作成処理 """
    return redirect(url_for('view', pk=0))

@app.route('/view/<id>')
def view(id):
    """ 参照画面 """
    return render_template('view.html', result={})


@app.route('/ja/view/<id>')
def view_ja(id):
    """ 参照画面 """
    return render_template('view_ja.html', result={})


@app.route('/random')
def random():
    """ ランダム参照処理 """
    return redirect(url_for('view', pk=0))


@app.route('/ja/random')
def random_ja():
    """ ランダム参照処理 """
    return redirect(url_for('view', pk=0))


if __name__ == '__main__':
    app.run()
