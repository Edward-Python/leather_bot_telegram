import sqlite3


class AdminDB:
    def __init__(self) -> None:
        self.db = sqlite3.connect("admin_db.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS admin_table(
                         id INTEGER PRYMARY KEY NOT NULL,
                         photo BLOB,
                         price INTEGER)''')
        self.db.commit()

    def add(self, photo, price):
        self.cur.execute("""INSERT INTO admin_table (photo, price)
                    VALUES (?, ?)""", (photo, price))
        self.db.commit()

    # def change(self, photo, change, price):
    #     pass

    # def delete(self, photo, change, price):
    #     pass
        
    # def add_photo(self, photo):
    #     pass

    # def add_change(self, change):
    #     pass

    # def add_price(self, price):
    #     pass

    # def change_photo(self, photo):
    #     self.cur.execute("""INSERT INTO admin_table (photo)
    #                      VALUES (?)""", (photo))
    #     self.db.commit()

    def change_change(self, change):
        pass
        # self.cur.execute("""INSERT INTO admin_table(change)
        #                  VALUES(?)""", (change))
        # self.db.commit()


    # def change_price(self, price):
    #     self.cur.execute("""INSERT INTO admin_table (price)
    #                      VALUES (?)""", (price))
    #     self.db.commit()