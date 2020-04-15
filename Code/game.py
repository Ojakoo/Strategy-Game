
class Game():
    def __init__(self, data):
        self.players = []
        self.level = None
        self.turn_num = data[0]
        self.turn_player = data[1]

    def set_level(self, level): 
        self.level = level

    def set_player(self, player):
        self.players.append(player)

    def all_units(self):
        units = []

        for player in self.players: 
            for unit in player.units:
                units.append(unit)

        return units