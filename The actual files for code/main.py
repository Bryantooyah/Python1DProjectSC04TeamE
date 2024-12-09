import os
import menu
#import singleplayer
from two_player.py import two_player
#import highscore

class main(object):
    def __init__(self):
        self.__menu = menu.main(self)

    def username(self):
        name = input("Enter your username: ")
        if name == "":
            print("Invalid username. Try again.")
            self.username()
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "high_score.txt")
            file = open(file_path, 'r')
            for line in file:
                if name == line: # Davin please make sure this works check username taken from leaderboard
                    print("Username already exists. Try again.")
                    self.username()
        return name
                
    def start(self):
        self.__menu.title_screen()
        name = self.username()
        return name
    
    def Menu(self, name):
        option = self.__menu.options(name)
        #if option == "1":
            #singleplayer.start()
        if option == "2":
            result = two_player()
            if result == "retry":
                two_player()
            elif result == "menu":
                #self.Menu(name) show menu
                pass

        # elif option == "3":
        #     #highscore.start()
        elif option == "4":
            self.__menu.settings(name)
        elif option == "5":
            self.__menu.exit()
        

master = main()
name = master.start()
master.Menu(name)