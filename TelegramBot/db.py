import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"

print(DB_PATH.resolve())

def subscribers():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE
    )
    ''')
    print(cursor.fetchall())
    conn.commit()
    cursor.execute("SELECT * FROM subscribers")
    print('Вывод таблицы', cursor.fetchall())

    conn.close()

def get_active_subscribers():
    subscribers()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM subscribers')
    result = cursor.fetchall()

    conn.close()
    return result

def add_subscriber(chat_id):
    subscribers()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO subscribers (user_id) VALUES (?)', (chat_id,))
    print('all good insert', chat_id)
    conn.commit()
    conn.close()

def remove_subscriber(chat_id):
    subscribers()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM subscribers WHERE user_id = ?', (chat_id,))
    conn.commit()
    conn.close()