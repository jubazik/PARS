from bs4 import BeautifulSoup


class HTMLParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    def parse(self):
        """
        Открывает фойл 'html_content' в формате html и читает код.
        Cоздает экземпляр класса BeautifulSoup передает ему аргумент для парсера html_content и парсит заголовок документа и сохраняет в переменную data
        :return:
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'lxml')
        self.data['number'] = soup.find('div').find("td", style='border: 1px solid black').text
        self.data['station'] = soup.find('p', align='left').text
        self.data['notification'] = "".join(soup.find('h3').text).split()[2]
        self.data['date'] = self._parse_date(soup.find('p', align='center').text)
        self.data['client_name'] = soup.find_all('p')[3].find("u").text
        self.data['place_of_transfer'] = soup.find_all('p')[3].find_all('u')[1].text
        self.data['locomotive'] = soup.find_all('p')[3].find_all('u')[2].text
        self.data['route_belonging'] = soup.find_all('p')[3].find_all('u')[3].text
        self.data['client_representative'] = soup.find_all('p')[8].find('u').text

        self._parse_table(soup.find_all("table")[1])

    def _parse_date(self, date_str):
        """
            Данная функция парсит дату с документа
        :param date_str:
        :return:
        """
        return date_str.replace("от", "").replace('час', ':').replace("мин", "").replace("г.", "")

    def _parse_table(self, table):
        """
        Данная функция парсит таблицу дакумента и сохраняет его в переменную data
        :param table:
        :return:
        """
        self.data['table_data'] = []
        for item in table.find_all("tr")[2:]:
            if item.text:
                row_data = {
                    'id': item.find_all("td")[0].text,
                    'wagon': item.find_all("td")[1].text,
                    'container_and_size': item.find_all("td")[2].text,
                    'type': item.find_all("td")[3].text,
                    'control_mark': item.find_all("td")[4].text,
                    'operation': item.find_all("td")[5].text,
                    'cargo_names': item.find_all("td")[6].text,
                    'note': item.find_all("td")[7].text
                }
                self.data['table_data'].append(row_data)

    def get_data(self):
        """
        Вывод всех данных
        :return:
        """
        return self.data
