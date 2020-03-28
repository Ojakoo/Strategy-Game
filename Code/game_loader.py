# function for generating game object from save file

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
    unit_list = []      #matrix of units each line contains unit data for one player

    # view gamedata
    print("gamedata:\n", gamedata,"\n")

    for line in file:
        line = line.strip("\n")

        if line == '#':
            break
        else:
            player_list.append(line.split(",")) # append player information

    # view collected player data
    print("player data:\n", player_list,"\n")

    for line in file:
        line = line.strip("\n")

        if line == '#':
            break
        else:
            typemap.append(line.split(",")) # append level data

    # view typemap read
    print("typemap read:\n", typemap,"\n")

    for line in file :
        line = line.strip("\n")

        if line == '#':
            break
        else:
            l = list(map(int, line.split(",")))

            x = [ l[0] ]

            for i in range(1, len(l), 3):  
                x.append( l[i:i + 3] )

            # zip unit data to easy iterate later
            unit_list.append(x)
                
    
    # view unit_data:
    print("collected unit_list from save file:\n",unit_list ,"\n")

    # all required data collected, close file
    file.close()

    game = Game(gamedata)
    
    #Set players
    for playerdata in player_list:
        player = Player(game, playerdata)
        game.set_player(player)

    #print players
    print("player objects:",game.players,"\n")

    #Set_Level(typemap)
    level = Level(game, typemap)
    game.set_level(level)

    #Set_Units(unitdata)
    # write new handler 
    for l in unit_list:
        player = game.players[ l[0] ] #get player object
        print("handled units for player",player.name,":")
        for u in range(1, len(l)):
            #unit init
            unit = Unit(l[u][0])
            unit.set_pos(l[u][1], l[u][2])
            unit.set_player(player)

            #set unit to game and table
            player.set_unit(unit)
            print(unit.type, unit.pos)

    return game


