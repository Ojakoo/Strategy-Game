
# tile init data

typedict_tile = {
    'p' : [1, True],
    'm' : [3, False],
    'c' : [1, True],
    'f' : [2, False]
}

class Tile():
    def __init__(self, tile_type, pos, level):
        self.level = level
        self.type = tile_type
        self.pos = pos #double (h, w)/ (y x) because python list
        self.unit = None
        
        self.mov_cost = typedict_tile[tile_type][0]
        self.see_through = typedict_tile[tile_type][1]

    def get_pos(self):
        return self.pos

    def set_unit(self, unit):
        self.unit = unit
