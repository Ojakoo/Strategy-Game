
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGraphicsScene, QApplication, QPushButton, QGraphicsView
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

        #self.showFullScreen()
        self.setGeometry(50,50,500,500)

        self.view.show() #is this needed?

    def init_Scene(self):

        # create scene to handle gi in
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0,0,2000,1000) #IMPLEMENT SCALING BY MAP!!, this is max size of scene

        # populate scene from self.game
        map = self.game.level.map

        for h in range(len(map)):
            for w in range(len(map[0])):
                obj = GITile(map[h][w])
                self.scene.addItem(obj.rect)

        # crete view and add to layout
        self.view = QGraphicsView(self.scene, self)
        self.view.adjustSize()
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