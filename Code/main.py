
import sys

from PyQt5.QtWidgets import QApplication
from gui_control import GuiControl


def main():
    global app
    app = QApplication(sys.argv)
    gui = GuiControl()
    gui.boot()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()