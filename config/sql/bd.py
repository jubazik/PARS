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
        query = '''
            SELECT d.*, c.*
            FROM documents d
            LEFT JOIN cargo c ON d.id = c.document_id
        '''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        result = {}
        for row in rows:
            document_id = row[0]  # Предполагается, что id документа — это первый элемент
            document_data = row[:10]  # Предполагается, что у документа 10 полей
            cargo_data = row[10:]  # Остальные поля — это данные о грузе

            if document_id not in result:
                result[document_id] = {
                    'document': document_data,
                    'cargo': []
                }

            if any(cargo_data):  # Проверяем, есть ли данные о грузе
                result[document_id]['cargo'].append(cargo_data)
        self.connection.commit()
        return result


    def get_notification_number(self, notification): # GET-Запрос по номеру документа Г-2б
        pass
    def get_nomber_cargo(self, wagon): # GET-Запрос выводит информацию о документе и связаные с ними вогоны
        query = '''
            SELECT d.*, c.*
            FROM documents d
            JOIN cargo c ON d.id = c.document_id
            WHERE c.document_id IN (
                SELECT document_id
                FROM cargo
                WHERE wagon = ?
            )
        '''

        self.cursor.execute(query, (wagon,))
        rows = self.cursor.fetchall()

        result = {}
        for row in rows:
            document = {
                'id': row[0],
                'number': row[1],
                'station': row[2],
                'notification': row[3],
                'date': row[4],
                'client_name': row[5],
                'place_of_transfer': row[6],
                'locomotive': row[7],
                'route_belonging': row[8],
                'client_representative': row[9],
            }
            cargo = {
                'id': row[10],
                'document_id': row[11],
                'wagon': row[12],
                'container_and_size': row[13],
                'type': row[14],
                'control_mark': row[15],
                'operation': row[16],
                'cargo_names': row[17],
                'note': row[18],
            }

            # Добавляем документ и соответствующий груз в словарь
            if tuple(document.items()) not in result:
                result[tuple(document.items())] = []
            result[tuple(document.items())].append(cargo)
        self.connection.commit()
        return result

    def close(self):
        self.connection.close()
