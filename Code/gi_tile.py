
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

class GITile(QGraphicsPixmapItem):
    
    def __init__(self, tile):
        super(GITile, self).__init__()
        self.tile = tile

        h = self.square.location[0]
        w = self.square.location[1]
        #tile_type = self.tile.type

        self.rect.setOffset((64 * h), (64 * w))

        #write function for fetching pixmap
        self.set_pixmap()

    def set_pixmap(self): 
        #set pixmap from resources
        self.setPixmap(QPixmap('resourcer/tile_placeholder.png'))
        
    def mousePressEvent(self, *args, **kwargs):
        pass
