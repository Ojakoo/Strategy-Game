from player import Player

class Game():
    def __init__(self, data):
        self.players = []
        self.level = None
        self.turn_num = data[0]
        self.turn_player = data[1]
        self.units = []

    def set_level(self, level):
        self.level = level

    def set_player(self,player):
        self.players.append(player)

    def set_unit(self, unit):
        self.units.append(unit)