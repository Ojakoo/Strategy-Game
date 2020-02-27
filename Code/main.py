import sys
import game_loader
from PyQt5.QtWidgets import QApplication
import gui

def main():
    game = game_loader.Load_Game("save_file.txt")
    app = QApplication(sys.arg)
    gui_game = gui.GUI(game)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()