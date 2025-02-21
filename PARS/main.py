import os
import tkinter
# From documents.g_2b
from config.parm import path_to_db
from config.sql.bd import *
from config.app import *
import tkinter as tk
from tkinter import messagebox, simpledialog



def get_downloads_folder():
    """Возвращает путь к папке загрузок пользователя в Windows."""
    return os.path.join(os.path.expanduser("~"), "Downloads")


FILE_NAME = 'PARS/null.html'
FILE_PATH = os.path.join(get_downloads_folder(), FILE_NAME)


def count_numbers(number):  # проверка количество цифр в вагоне
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



def document_gu_2b(file_name):
    db = Database(path_to_db)
    if not os.path.isfile(FILE_PATH):
        return clean_data(db.get_data_all())
    else:

        return  clean_data(db.get_data_all())

def documnet_gu_45():
    return "функция еще не разработана"


# логика построении программы
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Обработка данных")

    root.mainloop()