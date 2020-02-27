class Player():

    def __init__(self, game, data):
        self.name = data[0]
        self.ai = data[1]
        self.color = data[2]
        self.gold = data[3]
        self.game = game

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
