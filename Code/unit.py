
# storing init data and 

typedict_unit = {
    0 : [10,3],
    1 : [5,3]
}

class Unit():

    def __init__(self, unit_type):
        self.type = unit_type
        self.player = None
        self.pos = None #(h, w) double / (y x) because python list
        self.hp = typedict_unit[unit_type][0]
        self.ap = typedict_unit[unit_type][1]

    def set_pos(self, h, w):
        self.pos = (h, w)

    def set_player(self, owner):
        self.player = owner
