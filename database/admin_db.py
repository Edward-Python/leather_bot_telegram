import sqlite3


class AdminDB:
    def __init__(self) -> None:
        self.db = sqlite3.connect("admin_db.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS admin_table(
                         id INTEGER PRYMARY KEY,
                         photo BLOB,
                         photo1 BLOB,
                         photo2 BLOB,
                         photo3 BLOB,
                         change TEXT,
                         price INTEGER)''')
        self.db.commit()

    def add(self, photo, photo1, photo2, photo3, change, price):
        self.cur.execute("""INSERT INTO admin_table (
                         photo,
                         photo1,
                         photo2,
                         photo3,
                         change,
                         price)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (photo, photo1, photo2, photo3, change, price))
        self.db.commit()

    def photo_output(self):
        return self.cur.execute("""SELECT photo, photo1, photo2, photo3 
                         FROM admin_table""").fetchone()
    
    def photo_showcase(self):
        return self.cur.execute("""SELECT photo3 FROM admin_table""").fetchone()