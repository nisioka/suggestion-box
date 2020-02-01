import os
from flask import Flask, redirect, url_for, render_template, request, g
import sqlite3
import models

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db.sqlite3'),
    SECRET_KEY='hoge',
))


def connect_db():
    """ データベースに接続します """
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def get_db():
    """ connectionを取得します """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """ db接続をcloseします """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


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
    id = models.insert(get_db(), request.form['title'], request.form['title_ja'], request.form['description'],
                       request.form['description_ja'], request.form['author'])
    return redirect(url_for('view', id=id))


@app.route('/ja/create', methods=['POST'])
def create_ja():
    """ 新規作成処理 """
    id = models.insert(get_db(), request.form['title'], request.form['title_ja'], request.form['description'],
                       request.form['description_ja'], request.form['author'])
    return redirect(url_for('ja/view', id=id))


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
    return redirect(url_for('view', id=0))


@app.route('/ja/random')
def random_ja():
    """ ランダム参照処理 """
    return redirect(url_for('view', id=0))


if __name__ == '__main__':
    app.run()
