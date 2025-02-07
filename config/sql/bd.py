import sqlite3
class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEGER ,
                station TEXT,
                notification INTEGER UNIQUE,
                date TEXT,
                client_name TEXT,
                place_of_transfer TEXT,
                locomotive TEXT,
                route_belonging TEXT,
                client_representative TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cargo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id INTEGER,
                wagon TEXT,
                container_and_size TEXT,
                type TEXT,
                control_mark TEXT,
                operation TEXT,
                cargo_names TEXT,
                note TEXT,
                FOREIGN KEY (document_id) REFERENCES documents(id)
            )
        ''')
        self.connection.commit()

    def save_document(self, data): # сохраняет заголовок документа
        self.cursor.execute('''
            INSERT INTO documents (number, station, notification, date, client_name, place_of_transfer, locomotive, route_belonging, client_representative)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data['number'], data['station'], data['notification'], data['date'], data['client_name'], data['place_of_transfer'], data['locomotive'], data['route_belonging'], data['client_representative']))
        document_id = self.cursor.lastrowid
        self.connection.commit()
        return document_id

    def save_cargo(self, document_id, cargo_data): # Сохраняет таблицу вагонов и историю
        self.cursor.execute('''
            INSERT INTO cargo (document_id, wagon, container_and_size, type, control_mark, operation, cargo_names, note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (document_id, cargo_data['wagon'], cargo_data['container_and_size'], cargo_data['type'], cargo_data['control_mark'], cargo_data['operation'], cargo_data['cargo_names'], cargo_data['note']))
        self.connection.commit()

    def get_data_all(self): # GET-Запрос на вывод всю информацию из базы данных
        table_all = self.cursor.execute('''
            SELECT documents.*, cargo.*
            FROM documents
            JOIN cargo ON documents.id = cargo.document_id;  -- Используем 'id' из documents и 'document_id' из cargo
        ''').fetchall()
        self.connection.commit()
        return table_all

    def get_nomber_cargo(self, number_cargo): # GET-Запрос выводит информацию о документе и связаные с ними вогоны
        pass


    def close(self):
        self.connection.close()
