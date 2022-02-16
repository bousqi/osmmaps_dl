import sys
from PyQt5.QtWidgets import QApplication

from package.main_window import MainWindow


sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ex = MainWindow(app)
    ex.show()
    sys.exit(app.exec_())
