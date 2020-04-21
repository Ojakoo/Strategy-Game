
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import pyqtSignal, Qt

typedict_pixmap = {
    'p' : ['resources/plain.png'],
    'm' : ['resources/mountain.png'],
    'c' : ['resources/castle.png'],
    'f' : ['resources/forest.png']
}

class GITile(QGraphicsPixmapItem):
    
    def __init__(self, tile):
        super(GITile, self).__init__()
        self.tile = tile

        h = self.tile.pos[0]
        w = self.tile.pos[1]
        #tile_type = self.tile.type

        self.setOffset((64 * w), (64 * h))

        #write function for fetching pixmap
        self.set_pixmap()

    def set_pixmap(self):
        #set pixmap from resources
        self.setPixmap(QPixmap(typedict_pixmap[self.tile.type][0]))

    # most map related user interaction is via tile due to units and other always being on tiles
    # this way all handling of map events can be done with one function

    def mousePressEvent(self, event, *args, **kwargs):
        if event.button() == Qt.RightButton:
            self.tile.level.game.right_click_handler(self.tile)

        if event.button() == Qt.LeftButton:
            #self.highlight(event) #pitäis tää tunkkaa
            self.tile.level.game.set_chosen(self.tile)


