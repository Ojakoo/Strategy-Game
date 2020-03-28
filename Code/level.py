from tile import Tile

class Level():
    def __init__(self, game, typemap):
        self.game = game
        self.typemap = typemap
        
        height = len(typemap)
        width = len(typemap[0])

        self.map = [ [None for i in range(width)] for j in range(height)]

        for h in range(height):
            for w in range(width):
                tile_type = typemap[h][w]
                self.map[h][w] = Tile(tile_type, h, w)

        # view map after generating
        #print("Map in Level:",self.map,"\n")

        