def insert(con, title, title_ja, description, description_ja, author):
    """ INSERT処理 """
    cur = con.cursor()
    cur.execute(
        'insert into suggestions (title_en, title_ja, description_en, description_ja, author) values (?, ?, ?, ?, ?)',
        [title, title_ja, description, description_ja, author])

    id = cur.lastrowid
    con.commit()

    return id
