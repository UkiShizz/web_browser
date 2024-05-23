from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys

def main():
    try:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()
