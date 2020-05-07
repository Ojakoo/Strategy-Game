
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

typedict_pixmap = {
    0 : ['resources/swordsman_blue','resources/swordsman_red.png'],
    1 : ['resources/archer_blue.png', 'resources/archer_red.png'],
    2 : ['resources/mage_blue','resources/mage_red.png']
}

class GIUnit(QGraphicsPixmapItem):

    def __init__(self, unit, player_num):
        super(GIUnit, self).__init__()
        self.unit = unit

        pos = self.unit.tile.get_pos()

        self.set_pixmap(player_num)
        self.move(pos)
        
    def move(self, pos):
        self.setOffset((64 * pos[1]), (64 * pos[0]))

    def set_pixmap(self, player_num): 
        self.setPixmap(QPixmap(typedict_pixmap[self.unit.type][player_num]))


    # handles gi updates (move, statuses, etc)
    def update_item(self):
        self.move(self.unit.tile.get_pos())

    def remove_unit_gi(self):
        self.unit = None

            

