from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserEngine(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loadStarted.connect(self.on_load_started)
        self.loadFinished.connect(self.on_load_finished)

    def on_load_started(self):
        print("Загрузка началась")

    def on_load_finished(self, result):
        if result:
            print("Загрузка завершена")
        else:
            try:
                # Handle the error
                print("Ошибка загрузки: Страница не может быть загружена.")
            except Exception as e:
                print(f"Ошибка загрузки: {str(e)}")
