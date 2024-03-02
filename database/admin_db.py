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

    def photos_db(self):
        photo_album = self.cur.execute("""SELECT photo, photo1, photo2, photo3 
                         FROM admin_table""").fetchone()
        photos = []
        for photo in photo_album:
            photos.append(photo)
        return photos
    
    def showcase_photo_db(self):
        photo_sh_case = self.cur.execute("""SELECT photo FROM admin_table""").fetchone()
        scase = []
        for photo in photo_sh_case:
            scase.append(photo)
        return scase
    
    def description_db(self):
        desc = self.cur.execute("""SELECT change FROM admin_table""").fetchone()
        desc_product = []
        for description in desc:
            desc_product.append(description)
        return desc_product
    
    def price_db(self):
        price_prod = self.cur.execute("""SELECT price FROM admin_table""").fetchone()
        price_product = []
        for i in price_prod:
            price_product.append(i)
        return map(int, price_product)
