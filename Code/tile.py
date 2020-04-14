
# tile init data

typedict_tile = {
    'p' : [],
    'm' : [],
    'c' : [],
    'f' : []
}

class Tile():
    def __init__(self, tile_type, pos):
        self.type = tile_type
        self.pos = pos #double
        self.unit = None

    def get_position(self):
        return self.pos

    def spawn(self):
        pass

    def kill(self):
        pass