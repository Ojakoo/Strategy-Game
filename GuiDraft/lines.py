import sys
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView)

class TicTacToe(QGraphicsItem):
    # http://pyqt.sourceforge.net/Docs/PyQt5/api/QtWidgets/qgraphicsitem.html

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.board = [[None, None, None],[None, None, None], [None, None, None]]
        self.O = 0
        self.X = 1
        self.turn = self.O

    def boundingRect(self):
        # http://doc.qt.io/qt-5/qgraphicsitem.html#boundingRect
        return QRectF(0,0,300,300)

    def select(self, x, y):
        if x < 0 or y < 0 or x >= 3 or y >= 3:
            return
        if self.board[y][x] == None:
            self.board[y][x] = self.turn
            self.turn = 1 - self.turn

    def paint(self, painter, option, widget):
        # http://doc.qt.io/qt-5/qgraphicsitem.html#paint
        painter.setPen(Qt.black)
        painter.drawLine(0,100,300,100)
        painter.drawLine(0,200,300,200)
        painter.drawLine(100,0,100,300)
        painter.drawLine(200,0,200,300)
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == self.O:
                    painter.setPen(QPen(Qt.red, 3))
                    painter.drawEllipse(QPointF(50+x*100, 50+y*100), 35, 35)
                elif self.board[y][x] == self.X:
                    painter.setPen(QPen(Qt.blue, 3))
                    painter.drawLine(20+x*100, 20+y*100, 80+x*100, 80+y*100)
                    painter.drawLine(20+x*100, 80+y*100, 80+x*100, 20+y*100)

    def mousePressEvent(self, event):
        # http://doc.qt.io/qt-5/qgraphicsitem.html#mousePressEvent
        self.select(int(event.pos().x()/100), int(event.pos().y()/100))
        self.update()

class MainWindow(QGraphicsView):
    # http://pyqt.sourceforge.net/Docs/PyQt5/api/QtWidgets/qgraphicsview.html
    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene(self)
        self.tictactoe = TicTacToe()
        scene.addItem(self.tictactoe)
        scene.setSceneRect(0, 0, 300, 300)
        self.setScene(scene)
        self.show()