from game import Game
from level import Level
from player import Player
from unit import Unit

def Load_Game(save_file):
    #open and read data from save_file (typemap, players, units)

    file = open(save_file)

    gamedata = file.readline().strip("\n").split(",")    #general gamedata
    player_list = []    #list of players and data
    typemap = []        #matrix of map tiles and types
    unit_list = []      #list of units

    # view gamedata
    print("gamedata:\n", gamedata)

    for line in file:
        line = line.strip("\n")

        if line == '#':
            break
        else:
            player_list.append(line.split(",")) # append player information

    # view collected player data
    print("player data:\n", player_list)

    for line in file:
        line = line.strip("\n")

        if line == '#':
            break
        else:
            typemap.append(line.split(",")) # append level data

    #view typemap read
    print("typemap read:\n", typemap)
    
    for line in file:
        line = line.strip("\n")

        if line == '#':
            break
        else:
            unit_list = list(map(int, line.split(",")))
            #unitdata.append(line.split(","))

    game = Game(gamedata)
    
    print("works")
    
    #Set players

    for playerdata in player_list:
        player = Player(game, playerdata)
        game.set_player(player)

    #Set_Level(typemap)
    level = Level(game, typemap)
    game.set_level(level)

    #Set_Units(unitdata)
    for unitdata in unit_list:
        unit = Unit(unitdata[0])
        unit.set_player =  unitdata[1]
        unit.pos = (unitdata[2], unitdata[3])
        game.set_unit(unit)

    return game


