import os
import sys
from config.sql.bd import *
from model.g_2b import *


def get_downloads_folder():
    """Возвращает путь к папке загрузок пользователя в Windows."""
    return os.path.join(os.path.expanduser("~"), "Downloads")


def clean_data(data):
    """ Убираем \xa0 и лишние пробелы """
    cleaned_data = []
    for row in data:
        cleaned_row = [str(item).replace('\xa0', '').strip() for item in row]  #
        cleaned_data.append(cleaned_row)
    return cleaned_data


if __name__ == "__main__":
    # Определяем путь к файлу null.html в папке загрузок
    file_name = 'null.html'
    file_path = os.path.join(get_downloads_folder(), file_name)
    db_name = 'documents.db'
    db = Database(db_name)
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        print(f"Файл {file_path} не найден.")
        print("Вам показать данные:Да\Нет № вагон")
        user = input(":")
        if user.lower() == 'да':

            all_data = db.get_data_all()

            print("Данные из базы данных:")
            print(all_data)
        else:
            print(db.get_nomber_cargo(user))


        db.close()
        sys.exit(1)
    else:
        # Парсим HTML файл
        parser = HTMLParser(file_path)
        parser.parse()
        data = parser.get_data()

        # Сохраняем данные в базу данных

        document_id = db.save_document(data)

        for cargo in data['table_data']:
            db.save_cargo(document_id, cargo)

        # Удаляем файл после обработки
        os.remove(file_path)
        print(f"Файл {file_path} был удалён.")

        # Вывод данных
        db.close()
