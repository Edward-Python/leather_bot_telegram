import sqlite3


class UserDB:
    def __init__(self) -> None:
        self.db = sqlite3.connect("user_db.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user_table(
                         id INTEGER PRIMARY KEY NOT NULL,
                         user_id INTEGER,
                         full_name TEXT,
                         index_adress BLOB,
                         number_phon INTEGER)''')
        self.db.commit()

    def add_user(self, user_id, full_name, index_adress, number_phon):
        self.cur.execute('''INSERT INTO user_table(
                         user_id,
                         full_name,
                         index_adress,
                         number_phon)
                         VALUES (?, ?, ?, ?)''',
                         (user_id, full_name, index_adress, number_phon))
        self.db.commit()


user_db = UserDB()