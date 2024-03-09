import datetime

class Note:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now()
        self.last_modified = self.created_at

    def serialize(self):
        return {
            "title": self.title,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "body": self.body,
            "last_modified": self.last_modified.strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def deserialize(cls, data):
        return cls(data["title"], data["body"])

    def update(self, title, body):
        self.title = title
        self.body = body
        self.last_modified = datetime.datetime.now()

    def print_note(self):
        print("-" * 45)
        print(f"Создан: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}, Изменен: {self.last_modified.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Заголовок: {self.title}")
        print(self.body)
        print("-" * 45)