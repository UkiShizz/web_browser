import os
import json
from datetime import datetime

import os
import json
from datetime import datetime

class HistoryManager:
    def __init__(self, history_file="history.json"):
        self.history_file = history_file
        if not os.path.exists(self.history_file):
            self._initialize_history_file()

    def _initialize_history_file(self):
        with open(self.history_file, 'w') as file:
            json.dump([], file)

    def _read_history(self):
        with open(self.history_file, 'r') as file:
            return json.load(file)

    def _write_history(self, history):
        with open(self.history_file, 'w') as file:
            json.dump(history, file, indent=4)

    def add_entry(self, url, title):
        history = self._read_history()
        entry = {
            "url": url,
            "title": title,
            "timestamp": datetime.now().isoformat()
        }
        history.append(entry)
        self._write_history(history)

    def get_history(self):
        return self._read_history()

    def clear_history(self):
        self._write_history([])

# Пример использования (для тестирования)
if __name__ == '__main__':
    manager = HistoryManager()

    # Добавление записи
    manager.add_entry("http://www.example.com", "Example Website")
    
    # Получение истории
    history = manager.get_history()
    print("История просмотров:")
    for entry in history:
        print(f"{entry['timestamp']}: {entry['title']} ({entry['url']})")

    # Очистка истории
    manager.clear_history()
    print("История очищена.")
