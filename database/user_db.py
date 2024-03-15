import sqlite3


class UserDB:
    def __init__(self) -> None:
        self.db = sqlite3.connect("user_db.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user_table(
                         id INTEGER PRIMARY KEY NOT NULL,
                         id_product BLOB,
                         user_id INTEGER,
                         full_name TEXT,
                         index_adress BLOB,
                         number_phon INTEGER)''')
        self.db.commit()

    def add_user(self, id_product, user_id, full_name, index_adress, number_phon):
        self.cur.execute('''INSERT INTO user_table(
                         id_product,
                         user_id,
                         full_name,
                         index_adress,
                         number_phon)
                         VALUES (?, ?, ?, ?, ?)''',
                         (id_product, user_id, full_name, index_adress, number_phon))
        self.db.commit()


user_db = UserDB()