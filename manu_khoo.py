

def title_screen():
    print("\n=== Battle Ship ===")
    print("1. Single Player")
    print("2. Two Player")
    print("3. High Score")
    print("4. Settings")
    print("5. Quit")
    choice = input("Select an option (1-5): ")

    if choice == "1":
        print("Starting Single Player Mode...")
        # Call Max + Brandon's Single Player function
    elif choice == "2":
        two_player_mode() #ME + SANJAN
    elif choice == "3":
        pass
        # Call Davin's highscores
    elif choice == "4":
        pass
        settings() #MINE !!????
    elif choice == "5":
        exit()
    else:
        print("Invalid option. Try again.")
        title_screen()

# Settings
def settings():
    print("\n=== Settings ===")
    print("1. Adjust Sound")
    print("2. Set Username")
    print("3. View History Log")
    print("4. Back to Title Screen")
    choice = input("Select an option (1-4): ")

    if choice == "1":
        print("Sound settings.") #PLACEHOLDER??
        settings()
    elif choice == "2":
        username = input("Enter your username: ")
        print("Username set to {}.".format(username))
        print(username)
        settings()
    elif choice == "3":
        print("History Log: .") #PLACEHOLDER??
        settings()
    elif choice == "4":
        title_screen()
    else:
        print("Invalid option. Try again.")
        settings()



if __name__ == "__main__":
    title_screen()
