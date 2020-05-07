class Player():

    def __init__(self, game, data):
        self.name = data[0]
        self.ai = int(data[1])
        self.color = data[2]
        self.gold = int(data[3])
        self.game = game
        self.units = []
        self.castle = None
        self.controlled_tiles = []

    def set_castle(self, castle_tile):
        self.castle = castle_tile

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def set_unit(self, unit):
        self.units.append(unit)