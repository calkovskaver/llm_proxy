import sqlite3
from db.database import Database

### to vies stdout, run with -s option: 'python -m pytest -s tests/test_db.py'
def test_view_db():
    rows = Database.view_db()
    for row in rows:
        print(row)
