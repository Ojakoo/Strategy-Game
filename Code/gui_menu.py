
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QStackedLayout, QListWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

# currently MainWindow main layout is Stack nut later stack can be immersed to
# another layout and have that layout be the "theme" of Main menu where

class MainWindow(QMainWindow):

    switch_window = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.close()

        #these widgets are used as pages for the main menu
        self.Menu = QWidget()
        self.New_Game = QWidget()
        self.Load_Game = QWidget()
        self.Settings = QWidget()

        #stack layout handles page changes, now i can also implement a static menu view and
        #insert Stack to that layout
        self.Stack = QStackedLayout()
        self.Stack.addWidget(self.Menu)
        self.Stack.addWidget(self.New_Game)
        self.Stack.addWidget(self.Load_Game)
        self.Stack.addWidget(self.Settings)

        self.init_Menu()
        self.init_New_Game()
        self.init_Load_Game()
        self.init_Settings()

        self.setGeometry(50, 50, 300, 300)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.Stack)

    def init_Menu(self):
        menu_layout = QVBoxLayout()

        self.btn_new_game = QPushButton("New Game", self)
        self.btn_new_game.clicked.connect(self.make_display(1))
        menu_layout.addWidget(self.btn_new_game)

        self.btn_load_game = QPushButton("Load Game", self)
        self.btn_load_game.clicked.connect(self.make_display(2))
        menu_layout.addWidget(self.btn_load_game)

        self.btn_settings = QPushButton("Settings", self)
        self.btn_settings.clicked.connect(self.make_display(3))
        menu_layout.addWidget(self.btn_settings)

        self.Menu.setLayout(menu_layout)

    # init functions contain page layouts for different pages of main menu 
    # if we want to implement more pages for main menu we can just write new init and in Main Window
    # create new widget for it and add it to Stack and initialize it. make_display handles new page 
    # changes with just passing its index i in Stack.

    def init_New_Game(self):
        new_game_layout = QVBoxLayout()

        #Drop menu for maps
        #Player number choices, adds more of whats below
        #Player color choicem, human or ai choice

        self.btn_play = QPushButton("Play", self)
        self.btn_play.clicked.connect(self.play)
        new_game_layout.addWidget(self.btn_play)

        self.btn_menu = QPushButton("Back", self)
        self.btn_menu.clicked.connect(self.make_display(0))
        new_game_layout.addWidget(self.btn_menu)

        self.New_Game.setLayout(new_game_layout)

    def init_Load_Game(self):
        load_game_layout = QVBoxLayout()

        #Drop menu for save files
        #When save file selected play button appears

        self.btn_play = QPushButton("Play", self)
        self.btn_play.clicked.connect(self.play)
        load_game_layout.addWidget(self.btn_play)

        self.btn_menu = QPushButton("Back", self)
        self.btn_menu.clicked.connect(self.make_display(0))
        load_game_layout.addWidget(self.btn_menu)

        self.Load_Game.setLayout(load_game_layout)

    def init_Settings(self):
        settings_layout = QVBoxLayout()

        #volume and sound settings
        #key bindings

        self.btn_menu = QPushButton("Back", self)
        self.btn_menu.clicked.connect(self.make_display(0))
        settings_layout.addWidget(self.btn_menu)
        
        self.Settings.setLayout(settings_layout)

    # handles change of page via handing display function with index i to caller
    # this is done because pyqt signals dont carry arguments to functions so instead we
    # make a function changin page to index i when make_display is called

    def make_display(self, i):
        def display():
            self.Stack.setCurrentIndex(i)
        return display

    def play(self):
        print("emit")
        self.switch_window.emit()