from PyQt5.QtWidgets import QWidget, QVBoxLayout
from core.browser_engine import BrowserEngine

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.browser = BrowserEngine(self)
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)
