import os


def get_downloads_folder():
    """Возвращает путь к папке загрузок пользователя в Windows."""
    return os.path.join(os.path.expanduser("~"), "Downloads")


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

# class App:
#     def __init__(self, master):
#         self.master = master
#         master.title("Программа обработки данных")
#
#         # self.label = tk.Label(master, text="Выберите действие:")
#         # self.label.pack()
#
#         self.load_button = tk.Button(master, text="Гу_2Б", command=self.load_file)
#         self.load_button.pack()
#         self.load_button = tk.Button(master, text="Гу-45", command=self.load_file)
#         self.load_button.pack()
#         self.load_button = tk.Button(master, text="Поиск по номеру документа", command=self.load_file)
#         self.load_button.pack()
#
#         self.exit_button = tk.Button(master, text="Выход", command=master.quit)
#         self.exit_button.pack()
#
#     def load_file(self):
#         file_name = 'null.html'
#         file_path = os.path.join(get_downloads_folder(), file_name)
#
#         db = Database(path_to_db)
#         if not os.path.isfile(file_path):
#             pass
#             # messagebox.showerror("Ошибка", f"Файл {file_path} не найден.")
#
#             user_response = simpledialog.askstring("Ввод", "#вагона?")
#             try:
#                 if count_numbers(user_response) == 8:
#                     all_data = db.get_nomber_cargo(user_response)
#                     messagebox.showinfo("Данные из базы данных", (all_data))
#             except:
#                 messagebox.showinfo("Не верный номер вагона")
#
#         else:
#             parser = HTMLParser(file_path)
#             parser.parse()
#             data = parser.get_data()
#             document_id = db.save_document(data)
#
#             for cargo in data['table_data']:
#                 db.save_cargo(document_id, cargo)
#
#             os.remove(file_path)
#             messagebox.showinfo("Успех", f"Файл {file_path} был удалён.")
#
#         db.close()
#
#
# tk = tk
#
# app = App(tk)
