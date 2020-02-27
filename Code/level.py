from tile import Tile

class Level():
    def __init__(self, game, typemap):
        self.game = game

        height = len(typemap)
        width = len(typemap[0])

        self.map = [None] * height
        for h in typemap:
            self.map[h] = [None] * width
            for w in typemap[h]:
                tile_type = typemap[h][w]
                self.map[h][w] = Tile(tile_type, h, w)

        self.units = {}