
import sys

from PyQt5.QtWidgets import QApplication

from gui_game import GameWindow
from gui_menu import MainWindow

class GuiControl():

    def __init__(self):
        pass

    def show_Menu(self):
        self.menu_w = MainWindow()
        self.menu_w.switch_window.connect(self.show_Game)
        self.game_w.close()
        self.menu_w.show()

    def show_Game(self, game):
        self.game_w = GameWindow(game)
        self.game_w.switch_window.connect(self.show_Menu)
        self.menu_w.close()
        self.game_w.showFullScreen()
        #self.game_w.showFullScreen()

    def boot(self):
        self.menu_w = MainWindow()
        self.menu_w.switch_window.connect(self.show_Game)
        self.menu_w.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = GuiControl()
    controller.boot()
    sys.exit(app.exec_())