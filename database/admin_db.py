import sqlite3


class AdminDB:
    def __init__(self) -> None:
        self.db = sqlite3.connect("admin_db.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS admin_table(
                         id INTEGER PRYMARY KEY NOT NULL,
                         photo BLOB,
                         change TEXT,
                         price INTEGER)''')
        self.db.commit()

    def add(self, photo, change, price):
        self.cur.execute("""INSERT INTO admin_table (photo, change, price)
                    VALUES (?, ?)""", (photo, change, price))
        self.db.commit()