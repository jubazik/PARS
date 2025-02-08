import os
import sys
from config.sql.bd import Database
from model.g_2b import HTMLParser
from config.settings import path_to_db


def get_downloads_folder():
    """Возвращает путь к папке загрузок пользователя в Windows."""
    return os.path.join(os.path.expanduser("~"), "Downloads")


def count_numbers(number):  # проверка  количество цифр в вагоне
    numbers = str(number)
    if len(numbers) == 8:
        return True
    else:
        return False


def clean_data(data):
    """ Убираем \xa0 и лишние пробелы """
    cleaned_data = []
    for row in data:
        cleaned_row = [str(item).replace('\xa0', '').strip() for item in row]  #
        cleaned_data.append(cleaned_row)
    return cleaned_data


if __name__ == "__main__":
    exit_program = False  # Изменяем начальное значение на False
    while not exit_program:  # Цикл продолжается, пока exit_program False
        # Определяем путь к файлу null.html в папке загрузок
        file_name = 'null.html'
        file_path = os.path.join(get_downloads_folder(), file_name)

        db = Database(path_to_db)
        # Проверяем, существует ли файл
        if not os.path.isfile(file_path):
            print(f"Файл {file_path} не найден.")
            print("Вам показать данные: Да\Нет № вагон ")
            user = input(":")
            if user.lower() == 'да':
                all_data = db.get_data_all()
                print("Данные из базы данных:")
                print(all_data)
            elif count_numbers(user) == True:
                print(db.get_nomber_cargo(user))
            db.close()
            # Добавляем возможность выхода
            exit_command = input("Введите 'выход' для завершения программы или нажмите Enter для продолжения: ")
            if exit_command.lower() == 'выход':
                exit_program = True  # Устанавливаем флаг выхода
            continue  # Переходим к следующей итерации цикла

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
        # Добавляем возможность выхода
        exit_command = input("Введите 'выход' для завершения программы или нажмите Enter для продолжения: ")
        if exit_command.lower() == 'выход':
            exit_program = True  # Устанавливаем флаг выхода
