import sqlite3


class AdminDB:
    def __init__(self) -> None:
        self.db = sqlite3.connect("admin_db.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS admin_table(
                         id INTEGER PRYMARY KEY NOT NULL,
                         photo BLOB,
                         photo1 BLOB,
                         change BLOB,
                         price BLOB)''')
        self.db.commit()

    def add(self, photo, photo1, change, price):
        self.cur.execute("""INSERT INTO admin_table (photo, photo1, change, price)
                    VALUES (?, ?, ?, ?)""", (photo, photo1, change, price))
        self.db.commit()


    

    # def change(self, change):
    #     self.cur.execute("""INSERT INTO admin_table (change)
    #                 VALUES (?)""", (change))
    #     self.db.commit()

    # def price(self, price):
    #     self.cur.execute("""INSERT INTO admin_table (price)
    #                 VALUES (?)""", (price))
    #     self.db.commit()