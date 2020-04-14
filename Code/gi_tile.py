
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

import resources

class GITile(QGraphicsPixmapItem):
    
    def __init__(self, tile):
        super(GITile, self).__init__()
        self.tile = tile

        h = self.square.location[0]
        w = self.square.location[1]
        tile_type = self.tile.type

        self.rect.setOffset((64 * h), (64 * w))

        #write function for fetching pixmap
        self.set_pixmap()

    def set_pixmap(): 
        #set pixmap from resources
        self.setPixmap(QPixmap('resourcer/tile_placeholder.png'))
        pass
        
    def mousePressEvent(self, *args, **kwargs):
        return QtWidgets.QGraphicsRectItem.mousePressEvent(self, *args, **kwargs)
