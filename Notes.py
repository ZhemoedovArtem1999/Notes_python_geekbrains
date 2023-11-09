import json
import datetime

class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteApp:
    def __init__(self):
        self.notes = []
        self.currentId = 0

    def add_note(self, title, body):
        new_note = Note(self.currentId+1, title, body, str(datetime.datetime.now()))
        self.currentId+=1
        self.notes.append(new_note)
        self.save_notes()

    def edit_note(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.body = body
                note.timestamp = str(datetime.datetime.now())
                self.save_notes()
                return

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.save_notes()

    def save_notes(self):
        with open('notes.json', 'w') as file:
            notes_json = json.dumps([note.__dict__ for note in self.notes])
            file.write(notes_json)

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                notes_json = file.read()
                notes_list = json.loads(notes_json)
                self.notes = [Note(note['id'], note['title'], note['body'], note['timestamp']) for note in notes_list]
            for note in self.notes:
                if note.id > self.currentId:
                    self.currentId = note.id
        except FileNotFoundError:
            pass

    def show_notes(self):
        for note in self.notes:
            print(f"\nID заметки: {note.id} Время добавления: {note.timestamp}\nЗаголовок: {note.title}\n{note.body}\n")

if __name__ == "__main__":
    app = NoteApp()
    app.load_notes()

    while True:
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Посмотреть все заметки")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            app.add_note(title, body)
        elif choice == "2":
            id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок: ")
            body = input("Введите новое тело: ")
            app.edit_note(id, title, body)
        elif choice == "3":
            id = int(input("Введите ID заметки для удаления: "))
            app.delete_note(id)
        elif choice == "4":
            app.show_notes()
        elif choice == "5":
            break
        else:
            print("Такой команды нет!!!")