import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGraphicsScene, QApplication, QPushButton, QGraphicsView
from PyQt5.QtCore import pyqtSignal

class GameWindow(QMainWindow):

    switch_window = pyqtSignal()

    def __init__(self):
        super(GameWindow, self).__init__()
        self.setCentralWidget(QWidget())

        self.layout = QVBoxLayout()
        self.centralWidget().setLayout(self.layout)

        # for rendering needed objets and fetching data, implemented later
        #self.game = game

        self.init_Scene()
        self.init_GameUI()

        #self.showFullScreen()
        self.setGeometry(50,50,500,500)

        self.view.show()

    def init_Scene(self):
        self.scene = QGraphicsScene()

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
        print("emit")
        self.switch_window.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GameWindow()
    w.show()
    sys.exit(app.exec_())
