from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QUrl

class AddressBar(QLineEdit):
    def __init__(self, browser_tab, parent=None):
        super().__init__(parent)
        self.browser_tab = browser_tab
        self.setPlaceholderText("Enter URL and press Enter")
        self.returnPressed.connect(self.load_url)

    def load_url(self):
        url = self.text()
        if not url.startswith("http"):
            url = "http://" + url
        try:
            self.browser_tab.browser.setUrl(QUrl(url))
        except Exception as e:
            print(f"Error loading URL: {e}")
