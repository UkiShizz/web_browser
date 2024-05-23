from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from gui.browser_tab import BrowserTab
from gui.address_bar import AddressBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Web Browser")
        self.setGeometry(300, 300, 1024, 768)
        
        self.browser_tab = BrowserTab(self)
        self.address_bar = AddressBar(self.browser_tab)
        
        layout = QVBoxLayout()
        layout.addWidget(self.address_bar)
        layout.addWidget(self.browser_tab)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
