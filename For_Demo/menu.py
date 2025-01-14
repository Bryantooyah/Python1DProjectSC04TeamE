import highscore
## Title Screen
class main(object):
    def __init__(self, context):
        self.__context = context
        self.__historylog = highscore.HistoryLog(self)
    
    def title_screen(self):
        print(r"""
     ____        _   _   _           _     _       
    |  _ \      | | | | | |         | |   (_)      
    | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  
    |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
    |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                            | |    
                                            |_|    
    
    Created by Sanjan, Max, Brandon, Davin and Bryan^2 <3
    -----------------------------------------------------
    """)

    def options(self, name):
        print("\n=== Battle Ship ===")
        print("Welcome, {}!".format(name))
        print("1. Single Player")
        print("2. Two Player")
        print("3. High Score")
        print("4. Settings")
        print("5. Quit")
        choice = input("Select an option (1-5): ")
        

        if choice == "1":
            print("Starting Single Player Mode...")
            return "1"
            # Call Max + Brandon's Single Player function
        elif choice == "2":
            print("Starting Two Player Mode...")
            return "2"
            #ME + SANJAN
        elif choice == "3":
            return "3"
            # Call Davin's highscores
        elif choice == "4":
            return "4" # Call settings
        elif choice == "5":
            return "5"
        else:
            print("Invalid option. Try again.")
            return self.options(name)
        
    ## Settings
    def settings(self, name):
        print("\n=== Settings ===")
        print("1. Set Username")
        print("2. View History Log")
        print("3. Back to Title Screen")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            print("Setting new username...")
            new_name = self.__context.changeusername(name)
            return self.settings(new_name)

        elif choice == "2":
            print("Viewing History Log...")
            self.__historylog.display_history(name)
            return self.settings(name)
        
        elif choice == "3":
            print("Back to Title Screen.")
            self.__context.Menu(name)
        else:
            print("Invalid option. Try again.")
            return self.settings(name)


    ## Quit
    def exit(self):
        print("Goodbye!")
        quit()

    ## To do History Log + Sound Settings?
