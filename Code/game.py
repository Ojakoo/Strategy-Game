from PyQt5.QtCore import pyqtSignal, QObject
from unit import Unit
from ai import AI

typedict_unit_cost = {
    0 : 100,
    1 : 150,
    2 : 200
}

typedict_upgrades_cost = {
    0 : 100,
    1 : 200
}

class Game(QObject):

    turn_change = pyqtSignal()
    chosen_change = pyqtSignal()
    gi_update = pyqtSignal()
    game_ui_view = pyqtSignal()
    castle_view = pyqtSignal()
    blacksmith_view = pyqtSignal()
    village_view = pyqtSignal()
    game_end = pyqtSignal()
    new_unit = pyqtSignal()

    def __init__(self, data):
        super(Game, self).__init__()
        self.players = []
        self.level = None
        self.turn_num = int(data[0]) # move this inting to game loader
        self.turn_player = int(data[1])

        self.chosen_tile = None
        self.movable = None
        self.attackable = None
        self.winner = None
        self.spawn_tile = None

        self.ai = AI(self)

    def set_level(self, level): 
        self.level = level

    def set_player(self, player):
        self.players.append(player)

    def set_player_castle(self, tile):
        player = self.players[tile.state - 1]
        player.set_castle(tile)

    def check_win(self, tile):
        if tile.unit.player != self.players[tile.state - 1]:
            print("voitit pelin :)")
            self.winner = tile.unit.player
            self.game_end.emit()
            
    def next_turn(self):
        print("next turn")
        self.turn_player = self.turn_player + 1

        if self.turn_player >= len(self.players):
            self.turn_num = self.turn_num + 1
            self.turn_player = 0 # go to start of list players when turn_player is bigger than len
        
        self.players[self.turn_player].gold += 50

        for tile in self.players[self.turn_player].controlled_tiles:
            if tile.type == 'v':
                self.players[self.turn_player].gold += 25
        
        for unit in self.players[self.turn_player].units: # reset units
            unit.attacked = False
            unit.ap = unit.max_ap

        self.set_chosen(None)

        self.turn_change.emit()

        if self.players[self.turn_player].ai == 1:
            self.ai.control()

    def all_units(self):
        units = []

        for player in self.players: 
            for unit in player.units:
                units.append(unit)

        return units

    def set_chosen(self, tile):
        self.chosen_tile = tile

        if tile is not None and tile.unit is not None and tile.unit.player == self.players[self.turn_player]: # if owned unit get movable tiles 
            self.movable = self.level.get_movable(tile, tile.unit.ap)

            self.attackable = self.level.get_attackable(tile.unit)
        else:
            self.movable = None
            self.attackable = None
            
        self.chosen_change.emit()
        self.game_ui_view.emit()

    def chosen_tile_status(self):
        if self.chosen_tile is None: # no chosen tile
            return 0
        elif self.chosen_tile.unit is None: # chosen tile with no unit
            return 1
        elif self.chosen_tile.unit.player is self.players[self.turn_player]: # chosen tile with owned unit
            return 2
        else: # chosen tile with enemy unit
            return 3

    def move_unit(self, unit, new_tile):
        new_pos = new_tile.pos

        if self.movable[new_pos[0]][new_pos[1]][0]: # if unit is not able to move to that tile call is not executed
            unit.tile.unit = None
            unit.tile = new_tile
            unit.ap = unit.ap - self.movable[new_pos[0]][new_pos[1]][1]
            new_tile.unit = unit

            self.set_chosen(new_tile)

            self.gi_update.emit()

            if new_tile.type == 'c':
                self.check_win(new_tile)
            elif new_tile.type == 'v':
                for player in self.players:
                    if new_tile in player.controlled_tiles:
                        player.controlled_tiles.remove(new_tile)

                self.players[self.turn_player].controlled_tiles.append(new_tile)
                new_tile.set_state(self.turn_player)
                
                self.gi_update.emit()

        else:
            print("cant move there")

    def attack(self, unit, target):
        if target in self.attackable and unit.attacked is not True:
            unit.attacked = True
            target.hp = target.hp - round(unit.dmg * ((100 - target.arm)/100) )
            if target.hp <= 0:
                self.kill(target)
        else:
            print("not in attack range or unit already attacked")

    def spawn(self, unit_type):
        player = self.players[self.turn_player]
        cost = typedict_unit_cost[unit_type]

        if player.gold - cost >= 0:
            if self.spawn_tile.unit == None:
                player.gold = player.gold - cost

                new_unit = Unit(unit_type, self)
                new_unit.set_tile(self.spawn_tile)
                self.spawn_tile.set_unit(new_unit)
                new_unit.set_player(player)
                player.set_unit(new_unit)

                new_unit.ap = 0

                self.new_unit.emit()
                self.set_chosen(self.spawn_tile)

    def kill(self, unit):
        unit.set_status("Dead")
        
        unit.player.units.remove(unit)
        unit.tile.set_unit(None)

        self.gi_update.emit()
        
    def right_click_handler(self, clicked_tile):
        status = self.chosen_tile_status()

        if self.chosen_tile == clicked_tile:
            if status == 1:
                pass
            elif status == 2:
                pass
            elif status == 3: 
                pass
        else:
            if status == 0:
                pass
            elif status == 1:
                pass
            elif status == 2: # move / attack
                if clicked_tile.unit is None:
                    self.move_unit(self.chosen_tile.unit, clicked_tile)
                elif clicked_tile.unit is not None:
                    self.attack(self.chosen_tile.unit, clicked_tile.unit)
            elif status == 3: 
                pass

    def tile_func_caller(self, tile):
        tile_type = tile.type

        if tile_type == 'c':
            self.spawn_tile = tile
            self.castle_view.emit()
        elif tile_type == 'b':
            self.spawn_tile = tile
            self.blacksmith_view.emit()
        elif tile_type ==  'v':
            self.spawn_tile = tile
            self.village_view.emit()
        else:
            self.spawn_tile = None
            self.game_ui_view.emit()
        