import json
import os
from .note import Note

class NotesApp:
    def __init__(self):
        self.notes = []
        self.file_name = "data/notes.json"

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                data = json.load(file)
                self.notes = [Note.deserialize(note_data) for note_data in data]

    def save_notes(self):
        with open(self.file_name, "w") as file:
            data = [note.serialize() for note in self.notes]
            json.dump(data, file, indent=4)

    def add_note(self, title, body):
        note = Note(title, body)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, index, title, body):
        if 0 <= index < len(self.notes):
            self.notes[index].update(title, body)
            self.save_notes()
            print("Заметка успешно отредактирована.")
        else:
            print("Недопустимый индекс заметки.")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.save_notes()
            print("Заметка успешно удалена.")
        else:
            print("Недопустимый индекс заметки.")

    def list_notes(self, filter_date=None):
        for i, note in enumerate(self.notes):
            if filter_date is None or note.created_at.date() == filter_date.date():
                print(f"{i}: {note.title} - {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
                # print(f"{i}: {note.title} - {note.created_at}")

    def run(note):
        note.load_notes()
        while True:
            print("\nВыберите действие:")
            print("1. Показать все заметки")
            print("2. Добавить новую заметку")
            print("3. Распечатать заметку")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("0. Выход")
            choice = input("Введите номер действия: ")

            if choice == "1":
                note.list_notes()
            elif choice == "2":
                title = input("Введите заголовок заметки: ")
                body = input("Введите текст заметки: ")
                note.add_note(title, body)
            elif choice == "3":
                print()
                index = int(input("Введите номер заметки для печати: "))
                if 0 <= index < len(note.notes):
                    note.notes[index].print_note()
                    skip = input("Нажмите Enter чтобы продолжить")
                else:
                    print("Заметки с указанным индексом не существует. Пожалуйста, выберите другой индекс.")
            elif choice == "4":
                index = int(input("Введите номер заметки для редактирования: "))
                title = input("Введите новый заголовок заметки: ")
                body = input("Введите новый текст заметки: ")
                note.edit_note(index, title, body)
            elif choice == "5":
                index = int(input("Введите номер заметки для удаления: "))
                note.delete_note(index)
            elif choice == "0":
                break
            else:
                print("Неверный ввод, попробуйте снова.")