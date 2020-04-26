
# tile init data

typedict_tile = {
    'p' : [1, True],
    'm' : [3, False],
    'f' : [2, False],
    'c' : [1, True],
    'b' : [1, True],
    'v' : [1, True]
}

class Tile():
    def __init__(self, tile_type, pos, level):
        self.level = level
        self.type = tile_type
        self.pos = pos #double (h, w)/ (y x) because python list
        self.unit = None
        
        self.mov_cost = typedict_tile[tile_type][0]
        self.see_through = typedict_tile[tile_type][1]

        self.state = 0

    def get_pos(self):
        return self.pos

    def set_unit(self, unit):
        self.unit = unit

    def set_state(self, state):
        self.state = state

