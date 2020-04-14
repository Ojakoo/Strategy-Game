
import sys

from PyQt5.QtWidgets import QApplication

from gui_game import GameWindow
from gui_menu import MainWindow

class GuiControl():

    def __init__(self):
        pass

    def show_Menu(self):
        self.menu = MainWindow()
        self.menu.switch_window.connect(self.show_Game)
        self.game.close()
        self.menu.show()

    def show_Game(self):
        self.game = GameWindow()
        self.game.switch_window.connect(self.show_Menu)
        self.menu.close()
        self.game.show()

    def boot(self):
        self.menu = MainWindow()
        self.menu.switch_window.connect(self.show_Game)
        self.menu.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = GuiControl()
    controller.boot()
    sys.exit(app.exec_())