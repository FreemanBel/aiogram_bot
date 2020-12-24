class DbConnect():
    def connect(self):
        import sqlite3
        with sqlite3.connect('db.db') as conn:
            return conn

    def create_db(self, conn):
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS USERS (  
                    id          INTEGER PRIMARY KEY NOT NULL,
                    user_id     INTEGER NOT NULL,
                    username    TEXT,
                    password    TEXT,
                    UNIQUE(user_id)
                )
        ''')
        conn.commit()

    def insert(self, conn, user_id: int, username: str, password: str):
        c = conn.cursor()
        c.execute("""
                    INSERT OR IGNORE INTO USERS (
                    user_id, username, password
                    ) VALUES (?, ?, ?)""",
                  (user_id, username, password)
                  )
        conn.commit()
