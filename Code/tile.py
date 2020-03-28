
# tile init data
typedict_tile = {
    'p' : [],
    'm' : [],
    'c' : [],
    'f' : []
}

class Tile():
    def __init__(self, tile_type, h, y):
        self.tile_type = tile_type
        self.location = (h, y)
        self.unit = None