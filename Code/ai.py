
class AI():
    def __init__(self, game):
        self.game = game

    def control(self):
        print("ai active")
        player = self.game.players[self.game.turn_player]

        for unit in player.units:
            self.attack_priority(unit)
            closest = self.game.level.find_closest_movable(unit.tile, self.game.players[0].castle, unit.ap)
            self.game.move_unit(unit, closest)

            if not unit.attacked:
                self.attack_priority(unit)

        self.buy_unit(player, player.castle)
        
        for tile in player.controlled_tiles:
            if tile.unit == None:
                self.buy_unit(player, tile)

        if self.game.winner != None:
            self.game.game_end.emit()
        else:
            self.game.next_turn()

    def buy_unit(self, player, tile):
        self.game.spawn_tile = tile

        if player.gold >= 150:
            self.game.spawn(1)
        elif player.gold >= 100:
            self.game.spawn(0)

    def buy_upgrades(self):
        pass

    def attack_priority(self, unit):
        attackable = self.game.level.get_attackable(unit)
        self.game.attackable = attackable

        priority = None

        for a in attackable:
            if priority == None:
                priority = a
            elif priority.hp > a.hp:
                priority = a

        if priority != None:
            self.game.attack(unit, priority)
