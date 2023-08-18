from consoleUI import menu
from options import *

def console():
    while True:
        menu()
        user_input = input()
        if user_input == '1':
            print_notes("all")
        elif user_input == '2':
            print_notes("ID")
        elif user_input == '3':
            print_notes("date")
        elif user_input == '4':
            add_note()
        elif user_input == '5':
            print_notes("info")
            print()
            edit_note()
        elif user_input == '6':
            print_notes("info")
            print()
            del_note()
        elif user_input == '0':
            print("Программа завершена")
            break
        else:
            print("Некорректная команда, повторите ввод")



