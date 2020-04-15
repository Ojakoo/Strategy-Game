
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGraphicsScene, QPushButton, QGraphicsView, QGraphicsRectItem
from PyQt5.QtCore import pyqtSignal

from gi_unit import GIUnit
from gi_tile import GITile

class GameWindow(QMainWindow):

    switch_window = pyqtSignal()

    def __init__(self, game):
        super(GameWindow, self).__init__()
        self.game = game
        
        self.setCentralWidget(QWidget())

        self.layout = QVBoxLayout()
        self.centralWidget().setLayout(self.layout)

        self.init_Scene()
        self.init_GameUI()

        self.setGeometry(0,0,1920,1080)

    def init_Scene(self):

        # create scene to handle gi in
        self.scene = QGraphicsScene()

        # populate scene from self.game

        # tile generation
        game_map = self.game.level.map

        x = len(game_map[0]) * 64
        y = len(game_map) * 64
        self.scene.setSceneRect(0,0,x,y) #IMPLEMENT SCALING BY MAP!!, this is max size of scene

        for h in range(len(game_map)):
            for w in range(len(game_map[0])):
                obj = GITile(game_map[h][w])
                self.scene.addItem(obj)

        # unit generation
        
        units = self.game.all_units()

        for unit in units:
            obj = GIUnit(unit)
            self.scene.addItem(obj)  

        # crete view and add to layout
        self.view = QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()

        self.layout.addWidget(self.view)

    def init_GameUI(self):
        layout_ui = QHBoxLayout()

        self.btn_next_turn = QPushButton("Next Turn", self)
        #connect to func
        layout_ui.addWidget(self.btn_next_turn)

        self.btn_quit = QPushButton("Quit", self)
        self.btn_quit.clicked.connect(self.quit)
        layout_ui.addWidget(self.btn_quit)

        self.layout.addLayout(layout_ui)

    def quit(self):
        self.switch_window.emit()