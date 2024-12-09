import os
import copy

class TwoPlayerGame(object):
    def __init__(self):
        self.ship_sizes = [2, 2, 3, 3, 4]
        self.p1_grid = self.create_grid()
        self.p2_grid = self.create_grid()
        self.p1_ships = []
        self.p2_ships = []

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def create_grid():
        return [
            ["x","a","b","c","d","e","f","g","h"],
            ["1"," "," "," "," "," "," "," "," "],
            ["2"," "," "," "," "," "," "," "," "],
            ["3"," "," "," "," "," "," "," "," "],
            ["4"," "," "," "," "," "," "," "," "],
            ["5"," "," "," "," "," "," "," "," "],
            ["6"," "," "," "," "," "," "," "," "],
            ["7"," "," "," "," "," "," "," "," "],
            ["8"," "," "," "," "," "," "," "," "],
        ]

    @staticmethod
    def letter_to_num(letter):
        dictionary = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8}
        return dictionary.get(letter.lower(), -1)

    def insert_ship(self, length, starting_pos, orientation, grid):
        """Attempt to insert a ship into the grid.
        Returns (status, new_grid, ship_coords)."""
        if len(starting_pos) < 2:
            return "error", grid, None
        col = self.letter_to_num(starting_pos[0])
        try:
            row = int(starting_pos[1])
        except ValueError:
            return "error", grid, None

        original_grid = copy.deepcopy(grid)
        ship_coords = set()

        for _ in range(length):
            if 1 <= row <= 8 and 1 <= col <= 8 and grid[row][col] == " ":
                grid[row][col] = 's'
                ship_coords.add((row, col))
            else:
                return "error", original_grid, None
            if orientation == 'n':
                row -= 1
            elif orientation == 's':
                row += 1
            elif orientation == 'e':
                col += 1
            elif orientation == 'w':
                col -= 1

        return "success", grid, ship_coords

    @staticmethod
    def display_grid(grid, hide_ships=False):
        for row in grid:
            if hide_ships:
                print(" ".join(' ' if cell == 's' else cell for cell in row))
            else:
                print(" ".join(row))

    @staticmethod
    def check_win(grid):
        for row in grid:
            if 's' in row:
                return False
        return True

    def handle_hit(self, row, col, opponent_ships):
        """Remove the hit coordinate from the appropriate ship in opponent_ships.
        If a ship is completely destroyed, announce it."""
        for ship in opponent_ships:
            if (row, col) in ship:
                ship.remove((row, col))
                if len(ship) == 0:
                    print("You have sunk a ship!")
                    opponent_ships.remove(ship)
                break

    def player_turn(self, player, own_grid, opponent_grid, opponent_ships):
        self.clear_screen()
        self.print_instructions()
        print(f"Player {player}'s Turn\n")
        print("Your grid:")
        self.display_grid(own_grid)
        print("\nOpponent's grid:")
        self.display_grid(opponent_grid, hide_ships=True)

        while True:
            guess = input("\nEnter your guess (e.g., a1, c3): ").strip().lower()
            if len(guess) < 2:
                print("Invalid format, try again.")
                continue

            col = self.letter_to_num(guess[0])
            try:
                row = int(guess[1])
            except ValueError:
                print("Invalid format, try again.")
                continue

            if 1 <= row <= 8 and 1 <= col <= 8:
                if opponent_grid[row][col] == "s":
                    print("Hit!")
                    opponent_grid[row][col] = "x"
                    self.handle_hit(row, col, opponent_ships)
                    break
                elif opponent_grid[row][col] == " ":
                    print("Miss!")
                    opponent_grid[row][col] = "o"
                    break
                elif opponent_grid[row][col] in ["x", "o"]:
                    print("You already guessed here! Try again.")
                else:
                    print("Invalid guess. Try again.")
            else:
                print("Out of bounds. Try again.")

    @staticmethod
    def print_instructions():
        # Wartorn colors: alternate red and yellow lines
        battleship_ascii = [
            "  ____        _   _   _           _     _       ",
            " |  _ \\      | | | | | |         | |   (_)      ",
            " | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ",
            " |  _ < / _` | __| __| |/ _ \\/ __| '_ \\| | '_ \\ ",
            " | |_) | (_| | |_| |_| |  __/\\__ \\ | | | | |_) |",
            " |____/ \\__,_|\\__|\\__|_|\\___||___/_| |_|_| .__/ ",
            "                                          | |    ",
            "                                          |_|    "
        ]

        # Colors
        red = "\033[31m"
        yellow = "\033[33m"
        reset = "\033[0m"

        # Print the battleship ASCII in alternating red and yellow lines
        for i, line in enumerate(battleship_ascii):
            color = red if i % 2 == 0 else yellow
            print(color + line + reset)

        print("\n               WELCOME TO TWO PLAYER MODE\n")
        print("Instructions:")
        print("1. The grid is 8x8. Columns: a-h, Rows: 1-8.")
        print(f"2. Each player places 5 ships:")
        print(f"   - 2 ships of length \033[31m2\033[0m")
        print(f"   - 2 ships of length \033[31m3\033[0m")
        print(f"   - 1 ship of length \033[31m4\033[0m")
        print("3. To place a ship, enter a start position (e.g., 'a1') and orientation ('n', 's', 'e', 'w').")
        print("4. Ships cannot overlap or go outside the grid.")
        print("5. During your turn, guess a cell (e.g., 'c5'). 'x' is a hit, 'o' is a miss.")
        print("   Sink all opponent ships to win!")
        print("------------------------------------------------")

    @staticmethod
    def print_you_win():
        TwoPlayerGame.clear_screen()
        ascii_art = [
    "                                     |__",
    "                                     |\\/",
    "                                     ---",
    "                                     / | [",
    "                              !      | |||",
    "                            _/|     _/|-++'",
    "                        +  +--|    |--|--|_ |-",
    "                     { /|__|  |/\\__|  |--- |||__/",
    "                    +---------------___[}-_===_.'____                 /\\",
    "                ____`-' ||___-{]_| _[}-  |     |_[___\\==--            \\/   _",
    " __..._____--==/___]_|__|_____________________________[___\\==--____,------' .7",
    "|                                You win!!!                             BB-61/",
    " \\_________________________________________________________________________|"
        ]

        rainbow_colors = [
            "\033[31m", # Red
            "\033[33m", # Yellow
            "\033[32m", # Green
            "\033[36m", # Cyan
            "\033[34m", # Blue
            "\033[35m", # Magenta
        ]
        reset = "\033[0m"

        for i, line in enumerate(ascii_art):
            color = rainbow_colors[i % len(rainbow_colors)]
            print(color + line + reset)

    def run(self):
        # Clear the screen and print instructions at the start
        self.clear_screen()
        self.print_instructions()
        input("\nPress Enter to start the game...")

        # Player 1 places ships
        for size in self.ship_sizes:
            while True:
                self.clear_screen()
                self.print_instructions()
                print("\nPlayer 1, place your ship.")
                self.display_grid(self.p1_grid)
                print(f"\nYou need to place a ship of length \033[31m{size}\033[0m.")
                start = input("Enter the starting position (e.g., a1): ").strip().lower()
                orient = input("Enter orientation (n, s, e, w): ").strip().lower()
                result, self.p1_grid, coords = self.insert_ship(size, start, orient, self.p1_grid)
                if result == "success":
                    self.p1_ships.append(coords)
                    break
                else:
                    print("Invalid position or orientation. The ship was not placed. Try again.")
                    input("Press Enter to continue...")

        print("\nPlayer 1 is done placing ships. Press Enter once to hide the screen.")
        input()  # Press enter once
        self.clear_screen()
        print("Screen hidden. Press Enter again to proceed for Player 2.")
        input()  # Press enter twice
        self.clear_screen()

        # Reprint instructions for Player 2
        self.print_instructions()

        # Player 2 places ships
        for size in self.ship_sizes:
            while True:
                self.clear_screen()
                self.print_instructions()
                print("\nPlayer 2, place your ship.")
                self.display_grid(self.p2_grid)
                print(f"\nYou need to place a ship of length \033[31m{size}\033[0m.")
                start = input("Enter the starting position (e.g., a1): ").strip().lower()
                orient = input("Enter orientation (n, s, e, w): ").strip().lower()
                result, self.p2_grid, coords = self.insert_ship(size, start, orient, self.p2_grid)
                if result == "success":
                    self.p2_ships.append(coords)
                    break
                else:
                    print("Invalid position or orientation. The ship was not placed. Try again.")
                    input("Press Enter to continue...")


        print("\nPlayer 2 is done placing ships. Press Enter once to hide the screen.")
        input()  # Press enter once
        self.clear_screen()
        print("Screen hidden. Press Enter again to proceed with the game.")
        input()  # Press enter twice
        self.clear_screen()

        # Game loop
        while True:
            self.player_turn(1, self.p1_grid, self.p2_grid, self.p2_ships)
            # Hide the screen after Player 1's turn before Player 2's turn
            print("\nPlayer 1's turn complete. Press Enter once to hide the screen.")
            input()
            self.clear_screen()
            print("Screen hidden. Press Enter again to proceed to Player 2's turn.")
            input()
            self.clear_screen()

            if self.check_win(self.p2_grid):
                self.print_you_win()
                print("\nPlayer 1 wins!")
                break

            self.player_turn(2, self.p2_grid, self.p1_grid, self.p1_ships)
            # Hide the screen after Player 2's turn before Player 1's turn
            print("\nPlayer 2's turn complete. Press Enter once to hide the screen.")
            input()
            self.clear_screen()
            print("Screen hidden. Press Enter again to proceed to Player 1's turn.")
            input()
            self.clear_screen()

            if self.check_win(self.p1_grid):
                self.print_you_win()
                print("\nPlayer 2 wins!")
                break

        # After game ends, offer the option to retry or go back to menu
        while True:
            choice = input("\nGame Over! Would you like to (R)etry or go back to (M)enu?: ").strip().lower()
            if choice == 'r':
                return "retry"
            elif choice == 'm':
                return "menu"
            else:
                print("Invalid choice. Please type 'r' or 'm'.")
