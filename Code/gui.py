from PyQt5 import QtWidgets, QtCore, QtGui

class GUI(QtWidgets.QMainWindow):

    def __init__(self, game):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget)
        self.grid = QtWidgets.QGridLayout()
        self.centralWidget().setLayout(self.grid)

        self.game = game
        self.game_scene(game)

    def menu(self):
        # Menu wich is launched before launching game (possibly different file)
        return 0

    def game_scene(self, game):
        # Create render of

        self.setGeometry(0,0,1920,1080)
        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(10,10,500,500)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()