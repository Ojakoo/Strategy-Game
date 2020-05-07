
# storing init data 

# KEY(type) : [hp, ap, damage, range]
typedict_unit = {
    0 : [75,3,20,25,1],
    1 : [50,3,10,25,4],
    2 : [50,2,0,50,3]
}

class Unit():

    def __init__(self, unit_type, game):
        self.type = unit_type
        self.player = None
        self.tile = None #(h, w) double / (y x) because python list
        self.game = game
         
        self.max_hp = typedict_unit[unit_type][0]
        self.hp = self.max_hp
        self.max_ap = typedict_unit[unit_type][1]
        self.ap = self.max_ap

        self.arm = typedict_unit[unit_type][2]
        self.dmg = typedict_unit[unit_type][3]
        self.rng = typedict_unit[unit_type][4]

        self.attacked = False
        self.status = None
        
        self.set_status("Alive")

    def set_tile(self, tile):
        self.tile = tile

    def set_player(self, owner):
        self.player = owner

    def get_pos(self):
        return self.tile.get_pos()

    def set_status(self, status):
        self.status = status

