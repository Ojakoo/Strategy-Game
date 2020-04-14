import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton

#Gui classes below handle different functions of the menu and each contains needed widgets like buttons wich are needed

class Menu_GUI(QWidget):
    def __init__(self, parent=None):
        super(Menu_GUI, self).__init__(parent)

        self.btn_new_game = QPushButton("New Game", self)
        self.btn_new_game.move(150, 150)

        self.btn_load_game = QPushButton("Load Game", self)
        self.btn_load_game.move(150, 200)

        self.btn_settings = QPushButton("Settings", self)
        self.btn_settings.move(150, 250)

class New_Game_GUI(QWidget):
    def __init__(self, parent=None):
        super(New_Game_GUI, self).__init__(parent)

        #Drop menu for maps
        #Player number choices, adds more of whats below
        #Player color choicem, human or ai choice

        self.btn_menu = QPushButton("Back", self)
        self.btn_menu.move(150, 350)

class Load_Game_GUI(QWidget):
    def __init__(self, parent=None):
        super(Load_Game_GUI, self).__init__(parent)

        #Drop menu for save files
        #When save file selected play button appears

        self.btn_menu = QPushButton("Back", self)
        self.btn_menu.move(150, 350)

class Settings_GUI(QWidget):
    def __init__(self, parent=None):
        super(Settings_GUI, self).__init__(parent)

        #volume and sound settings
        #key bindings

        self.btn_menu = QPushButton("Back", self)
        self.btn_menu.move(150, 350)

#Main Window handeles menu events and menu view is determined by its CentralWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(760, 340, 400, 400)
        self.start_Menu()

        #write def InitUI() for init handling of main windowA

        #carries settings vector wich vill be brought to game session and modified in settings, also modifiable in game?

#functions of MainWindow handle changing of central widget and buttons and such created by Gui classes are connected here 
#to needed functions to allow changing of windows

    def start_Menu(self):
        self.Menu = Menu_GUI(self) #set menu as central widgets
        self.setCentralWidget(self.Menu)

        self.Menu.btn_load_game.clicked.connect(self.start_Load_Game)
        self.Menu.btn_new_game.clicked.connect(self.start_New_Game)
        self.Menu.btn_settings.clicked.connect(self.start_Settings)

        self.show()

    def start_Load_Game(self):
        self.Load_Game = Load_Game_GUI(self) #set load game as central widgets
        self.setCentralWidget(self.Load_Game)

        self.Load_Game.btn_menu.clicked.connect(self.start_Menu)

        self.show()

    def start_New_Game(self):
        self.New_Game = New_Game_GUI(self) #set new game as central widgets
        self.setCentralWidget(self.New_Game)
        
        self.New_Game.btn_menu.clicked.connect(self.start_Menu)

        self.show()

    def start_Settings(self):
        self.Settings = Settings_GUI(self) #set settings as central widgets
        self.setCentralWidget(self.Settings)

        self.Settings.btn_menu.clicked.connect(self.start_Menu)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())