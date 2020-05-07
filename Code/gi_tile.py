
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

typedict_pixmap = {
    'p' : ['resources/plain.png','resources/tile_placeholder.png'],
    'm' : ['resources/mountain.png'],
    'f' : ['resources/forest.png'],
    'c' : ['','resources/castle_blue.png','resources/castle_red.png'],
    'b' : ['resources/tile_placeholder.png'],
    'v' : ['resources/village.png','resources/village_blue.png','resources/village_red']
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
        self.setPixmap(QPixmap(typedict_pixmap[self.tile.type][self.tile.state]))

    # most map related user interaction is via tile due to units and other always being on tiles
    # this way all handling of map events can be done with one function

    def mousePressEvent(self, event, *args, **kwargs):
        if event.button() == Qt.RightButton:
            self.tile.level.game.right_click_handler(self.tile)

        if event.button() == Qt.LeftButton:
            #self.highlight(event) #pitäis tää tunkkaa
            self.tile.level.game.set_chosen(self.tile)

    def mouseDoubleClickEvent(self, event, *args, **kwarga):
        self.tile.level.game.tile_func_caller(self.tile)

