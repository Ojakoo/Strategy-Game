
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

import resources

class GIUnit(QGraphicsPixmapItem):
    def __init__(self, unit):
        super(UnitGI, self).__init__()
        self.unit = unit

        pos = sulf.unit.pos
        unit_type = self.unit.type

        self.setPixmap(QPixmap('resourcer/unit_placeholder.png'))
        
    def move(self, pos):
        self.rect.setOffset((64 * pos[0]), (64 * pos[1]))


        

 