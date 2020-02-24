#!/usr/bin/python
# -*- coding: utf-8 -*-


def insert(con, title, title_ja, description, description_ja, author):
    """ INSERT処理 """
    cur = con.cursor()
    cur.execute(
        'insert into suggestions (title_en, title_ja, description_en, description_ja, author) values (?, ?, ?, ?, ?)',
        [title, title_ja, description, description_ja, author])

    id = cur.lastrowid
    con.commit()

    return id


def select(con, id):
    """ 指定したキーのデータをSELECTする """
    cur = con.execute(
        'select id, title_en, title_ja, description_en, description_ja, author, created from suggestions where id=?',
        (id,))
    return cur.fetchone()


def select_all_en(con):
    """ SELECTする """
    cur = con.execute(
        'select id, case when length(title_en) > 0 then title_en else title_ja end as title,'
        'substr(case when length(description_en) > 0 then description_en else description_ja end, 1, 25) || "..." as description,'
        'author, created from suggestions order by created desc')
    return cur.fetchall()


def select_all_ja(con):
    """ SELECTする """
    cur = con.execute(
        'select id, case when length(title_ja) > 0 then title_ja else title_en end as title,'
        'substr(case when length(description_ja) > 0 then description_ja else description_en end, 1, 25) || "..." as description,'
        'author, created from suggestions order by created desc')
    return cur.fetchall()
