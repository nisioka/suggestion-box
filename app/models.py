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
        'select id, case when title_en is not NULL then title_en else title_ja end as title,'
        'substr(case when description_en is not NULL then description_en else description_ja end, 1, 25) || "..." as description,'
        'author, created from suggestions order by created desc')
    return cur.fetchall()
