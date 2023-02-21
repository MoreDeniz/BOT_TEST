import sqlite3

class DataBase:
    db_path = None

    def __int__(self, db_path: str = 'data_base/pa_db.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users
        (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER,
        name VARCHAR,
        description VARCHAR,
        location_id INTEGER,
        promoter_id INTEGER,
        date VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_events(self):
        sql = '''CREATE TABLE IF NOT EXISTS events
        (event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        location_id INTEGER,
        user_id INTEGER,
        date VARCHAR,
        price REAL)'''
        self.execute(sql, commit=True)

    def create_table_locations(self):
        sql = '''CREATE TABLE IF NOT EXISTS events
        (location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        city VARCHAR,
        address VARCHAR,
        phone VARCHAR,
        url VARCHAR)'''
        self.execute(sql, commit=True)

    def disconnect(self):
        self.connection.close()



