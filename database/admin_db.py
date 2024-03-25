import sqlite3


class AdminDB:
    def __init__(self) -> None:
        self.db = sqlite3.connect("admin_db.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS admin_table (
                         id INTEGER PRIMARY KEY NOT NULL,
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

    def product_delete(self, id):
        product_del = self.cur.execute(f"""DELETE FROM admin_table WHERE id=={id}""").fetchall()
        self.db.commit()
        return product_del
    
    def showcase_photo_db(self):
        photo_sh_case = self.cur.execute("""SELECT id, photo FROM admin_table""").fetchall()
        return photo_sh_case
    
    def photos_db(self):
        photo_album = self.cur.execute("""SELECT id, photo, photo1, photo2, photo3 
                         FROM admin_table""").fetchall()
        return photo_album
    
    def description_db(self):
        desc = self.cur.execute("""SELECT id, change FROM admin_table""").fetchall()        
        return desc
    
    def price_db(self):
        price_prod = self.cur.execute("""SELECT id, price FROM admin_table""").fetchall()
        return price_prod
    

admin_db = AdminDB()