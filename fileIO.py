from Note import Note

def write(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(notes.to_string())
        file.write('\n')
    file.close()

def read():
    global notes_list
    try:
        notes_list = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note(id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            notes_list.append(note)
    except Exception:
        print('Список заметок пуст')
    finally:
        return notes_list
