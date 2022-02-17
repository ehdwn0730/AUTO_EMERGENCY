import sqlite3

def insert(id):
    # SQLite DB 연결
    conn = sqlite3.connect("web/db.sqlite3")

    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    sql = "insert into board_situation(client_id_id) values (?)"
    cur.execute(sql, (id))
    conn.commit()

    conn.close()