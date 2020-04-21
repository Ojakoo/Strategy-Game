
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

import resources

class GIUnit(QGraphicsPixmapItem):

    def __init__(self, unit):
        super(GIUnit, self).__init__()
        self.unit = unit

        pos = self.unit.tile.get_pos()

        self.set_pixmap()
        self.move(pos)
        
    def move(self, pos):
        self.setOffset((64 * pos[1]), (64 * pos[0]))

    def set_pixmap(self): 
        #set pixmap from resources
        #unit_type = self.unit.type # used in pixmap setting
        self.setPixmap(QPixmap('resources/unit_placeholder.png'))

    # handles gi updates (move, statuses, etc)
    def update(self):
        self.move(self.unit.tile.get_pos())

    def remove_unit_gi(self):
        self.unit = None

            

