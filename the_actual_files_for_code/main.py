import os
import menu
import singleplayer
import two_player
import highscore
import csv

class main(object):
    def __init__(self):
        self.__menu = menu.main(self)
        self.__two_player = two_player.TwoPlayerGame()
        self.__highscore = highscore.High_Score(self)
        self.__singleplayer = singleplayer.main()

    ## Create Username at Start
    def username(self):
        name = input("Enter your username: ")
        if name == "":
            print("Invalid username. Try again.")
            return self.username()
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "high_score.csv")
            file = open(file_path, 'r')
            converted_file = csv.reader(file)
            for line in converted_file:
                if line == []:
                    continue
                elif name == line[0]:
                    print("Username already exists. Try again.")
                    return self.username()
            return name
    
    ## Change Username
    def changeusername(self, name):
        new_name = input("Enter your username: ")
        if new_name == "":
            print("Invalid username. Try again.")
            return self.changeusername(name)
        elif new_name == name:
            print("Username is the same. Try again.")
            return self.changeusername(name)
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "high_score.csv")
            file = open(file_path, 'r')
            converted_file = csv.reader(file)
            for line in converted_file:
                if line == []:
                    continue
                elif name == line[0]:
                    print("Username already exists. Try again.")
                    return self.changeusername(name)
            return new_name
        
    ## Start Menu
    def start(self):
        self.__menu.title_screen()
        name = self.username()
        return name
    ## Menu
    def Menu(self, name):
        option = self.__menu.options(name)
        if option == "1":
            single_result = self.__singleplayer.play_game()
            self.__highscore.save_score(name, single_result[0], single_result[1], "singleplayer", single_result[2])
            return self.Menu(name)
        elif option == "2":
            twoplayer_result = self.__two_player.run()
            self.__highscore.save_score(name, '0', twoplayer_result, "twoplayer", 'None')
            return self.Menu(name)

        elif option == "3":
            self.__highscore.display_high_score()
            return self.Menu(name)
        elif option == "4":
            self.__menu.settings(name)
        elif option == "5":
            self.__menu.exit()
        
## Running Main
master = main()
name = master.start()
master.Menu(name)