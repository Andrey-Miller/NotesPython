from datetime import datetime
import counter as counter

class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self):
        return str(self.id)

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_id(self):
        self.id = str(counter.set_id())

    def set_title(self, string):
        self.title = string

    def set_body(self, string):
        self.body = string

    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self):
        return str(self.id) + ';' + self.title + ';' + self.body + ';' + self.date

    def notes_list(self):
        return '\nID: ' + str(self.id) + '\n' + 'Заголовок: ' + self.title + '\n' + 'Описание: ' + self.body + '\n' + 'Дата добавления: ' + self.date



