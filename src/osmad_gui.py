import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from package.main_window import MainWindow


sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook


if __name__ == "__main__":
    app = QApplication(sys.argv)

    pixmap = QPixmap(":/img/resources/base/maps.png").scaledToWidth(384, QtCore.Qt.SmoothTransformation)
    splash = QSplashScreen(pixmap)
    splash.show()

    ex = MainWindow(app)
    ex.show()
    splash.finish(ex)

    sys.exit(app.exec_())
