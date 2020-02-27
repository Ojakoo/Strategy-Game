import game_loader

#tester for game_loader function

def main():
    print("testing")

    game = game_loader.Load_Game("save_file.txt")

    print("game Object init successful")

    print(game.players)
    print(game.level.typemap)

if __name__ == '__main__':
    main()