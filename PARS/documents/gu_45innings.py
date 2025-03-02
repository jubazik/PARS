from bs4 import BeautifulSoup


class HTMLParserGu45Innings:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    def parser_gu45_innings(self):
        with open(self.file_path, 'r', encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'lxml')
        data = "".join(soup.find('h3').text).split()
        self.data['number'] = data[3]
        self.data['']
        return self.data



