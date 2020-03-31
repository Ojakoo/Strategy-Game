from game_loader import Load_Game
from game_saver import Save_Game 

#tester for game_loader function

def main():
    print("testing\n")

    game = Load_Game("save_file.txt")

    print("game Object init successful")
    
    print(game.players,"\n")
    print(game.level.typemap,"\n")

    Save_Game(game)


if __name__ == '__main__':
    main()
    