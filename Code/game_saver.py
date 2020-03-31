# function for generating new save file from game object

def Save_Game(game):

    file = open("new_save_file.txt", "w")

    file.write( str(game.turn_num) + "," + str(game.turn_player) + "\n" )

    for player in game.players:
        file.write( player.name + "," + str(player.ai) + "," + str(player.color) + "," + str(player.gold) + "\n" )

    file.write("#\n")

    typemap = game.level.typemap

    for h in range( len(typemap) ):
        s = typemap[h][0]

        for w in range( 1, len(typemap[0]) ):
            if s != None:
                s = s + "," + typemap[h][w]

        file.write( s + "\n")

    file.write("#\n")

    for i in range(len(game.players)):
        s = str(i)
        for unit in game.players[i].units:
            s = s + "," + str(unit.type) + "," + str(unit.pos[0]) + "," + str(unit.pos[1]) 

        file.write( s + "\n" )

    file.write("#")

    print("Game succesfully saved.\n")

    file.close