from PyQt5.QtCore import pyqtSignal, QObject

class Game(QObject):

    turn_change = pyqtSignal()
    chosen_change = pyqtSignal()
    gi_update = pyqtSignal()

    def __init__(self, data):
        super(Game, self).__init__()
        self.players = []
        self.level = None
        self.turn_num = int(data[0]) # move this inting to game loader
        self.turn_player = int(data[1])

        self.chosen_tile = None
        self.movanle = None

    def set_level(self, level): 
        self.level = level

    def set_player(self, player):
        self.players.append(player)

    def next_turn(self):
        self.turn_player = self.turn_player + 1

        if self.turn_player >= len(self.players):
            self.turn_num = self.turn_num + 1
            self.turn_player = 0 # go to start of list players when turn_player is bigger than len

        for unit in self.players[self.turn_player].units: # reset units
            unit.attacked = False
            unit.ap = unit.max_ap

        self.set_chosen(None)

        self.turn_change.emit()

    def all_units(self):
        units = []

        for player in self.players: 
            for unit in player.units:
                units.append(unit)

        return units

    def set_chosen(self, tile):
        self.chosen_tile = tile

        if tile != None and tile.unit != None and tile.unit.player == self.players[self.turn_player]: # if owned unit get movable tiles 
            self.movable = self.level.get_movable(tile, tile.unit.ap)
            
            for a in self.movable:
                print(a)
            print("")

            self.attackable = self.level.get_attackable(tile.unit)
        else:
            self.movable = None
            
        self.chosen_change.emit()

    def chosen_tile_status(self):
        if self.chosen_tile == None: # no chosen tile
            return 0
        elif self.chosen_tile.unit == None: # chosen tile with no unit
            return 1
        elif self.chosen_tile.unit.player == self.players[self.turn_player]: # chosen tile with owned unit
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
        
        else:
            print("cant move there")

    def attack(self, unit, target):
        if target in self.attackable:
            target.hp = target.hp - round(unit.dmg * ((100 - target.arm)/100) )
            if target.hp <= 0:
                print("hp < 0 ")
                self.kill(target)
            print("attack with damage:",round(unit.dmg * ( (100 - target.arm)/100 ) ) ) 
        else:
            print("not in attack range")

    def kill(self, unit):
        unit.set_status("Dead")
        
        player.units.remove(unit)
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
                if clicked_tile.unit == None:
                    self.move_unit(self.chosen_tile.unit, clicked_tile)
                elif clicked_tile.unit != None:
                    self.attack(self.chosen_tile.unit, clicked_tile.unit)
            elif status == 3: 
                pass


        
