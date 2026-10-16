import sqlite3
from config import config

class Database:

    @staticmethod
    def connect():
        return sqlite3.connect(config.DATABASE)

    @staticmethod
    def init_database():
        conn = Database.connect()

        create_table_stmt = "CREATE TABLE IF NOT EXISTS proxy_data" \
        "(id INTEGER PRIMARY KEY AUTOINCREMENT)," \
        "key TEXT," \
        "user TEXT," \
        "model TEXT," \
        "tokens_limit INTEGER," \
        "tokens_used INTEGER," \
        "risk_prompts INTEGER,"


        cursor = conn.cursor()

