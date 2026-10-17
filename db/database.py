import sqlite3
from config import config

class Database:

    @staticmethod
    def connect():
        return sqlite3.connect(config.DATABASE)

    @staticmethod
    def init_database():
        conn = Database.connect()

        create_table_stmt_data = "CREATE TABLE IF NOT EXISTS proxy_data" \
        "(id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "key text," \
        "user text," \
        "model text," \
        "tokens_limit INTEGER," \
        "tokens_used INTEGER," \
        "risk_prompts INTEGER)"

        create_table_stmt_log = "CREATE TABLE IF NOT EXISTS log" \
        "(id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "user text," \
        "model text," \
        "tokens_used INTEGER," \
        "created_at DATE)"


        cursor = conn.cursor()
        cursor.execute(create_table_stmt_data)
        cursor.execute(create_table_stmt_log)

        conn.commit()
        conn.close()

    @staticmethod
    def insert_log(user, model, tokens, date):
        conn = Database.connect()

        insert_stmt = "INSERT INTO log (user, model, tokens_used, created_at)" \
        "VALUES (?, ?, ?, ?)"

        cursor = conn.cursor()
        cursor.execute(insert_stmt, (user, model, tokens, date))

        conn.commit()
        conn.close()

    @staticmethod
    def view_db():
        conn = Database.connect()

        select_stmt = "SELECT * from log"

        cursor = conn.cursor()
        cursor.execute(select_stmt)

        rows = cursor.fetchall()

        conn.close()

        return rows

