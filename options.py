import fileIO as IO
from Note import *

def add_note():
    title = input("Заголовок:\n")
    body = input("Описание:\n")
    note = Note(id=counter.set_id(), title=title, body=body, date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")))
    notes_list = IO.read()
    current_ids = []
    for n in notes_list:
         current_ids.append(n.get_id())
    for i in current_ids:
        if note.get_id() in current_ids:
            note.set_id()
    notes_list.append(note)
    IO.write(notes_list, 'a')
    print("Заметка добавлена")

def del_note():
    notes_list = IO.read()
    if notes_list:
        id = input("Введи ID заметки для удаления: ")
        flag = False
        for i in notes_list:
            if id == i.get_id():
                notes_list.remove(i)
                counter.id = 0
                flag = True
        if flag:
            IO.write(notes_list, 'a')
            print("Заметка удалена")
        else:
            print("Нет заметки с данным ID")

def edit_note():
    notes_list = IO.read()
    if notes_list:
        id = input("Введи ID заметки для изменения: ")
        flag = False
        notes_list_new = []
        for i in notes_list:
            if id == i.get_id():
                flag = True
                i.set_title(input("Новый заголовок:\n"))
                i.set_body(input("Новое описание:\n"))
                i.set_date()
            notes_list_new.append(i)
        if flag:
            IO.write(notes_list_new, 'a')
            print("Заметка с ID: ", id, " изменена")
        else:
            print("Нет заметки с данным ID")

def print_notes(type):
    notes_list = IO.read()

    if notes_list:
        if type == "all":
            print("СПИСОК ЗАМЕТОК:")
            for i in notes_list:
                print(i.notes_list())
            print()

        if type == "info":
            for i in notes_list:
                print("ID: ", i.get_id(), " | Заголовок: ", i.get_title())

        elif type == "ID":
            for i in notes_list:
                print("ID: ", i.get_id(), " | Заголовок: ", i.get_title())
            id = input("\nВведи ID заметки, чтобы вывести полную информацию: ")
            flag = True
            for i in notes_list:
                if id == i.get_id():
                    print(i.notes_list())
                    print()
                    flag = False
            if flag:
                print("Нет заметки с данным ID")

        elif type == "date":
            date = input("Введи дату в формате: DD.MM.YYYY: ")
            flag = True
            for i in notes_list:
                date_note = str(i.get_date())
                if date == date_note[:10]:
                    print(i.notes_list())
                    print()
                    flag = False
            if flag:
                print("Нет заметок за указанную дату")







