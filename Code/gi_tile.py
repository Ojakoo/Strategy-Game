
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

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
        self.setPixmap(QPixmap('resources/tile_placeholder.png'))
        
