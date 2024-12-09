import os
import copy

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def letter_to_num(letter):
    dictionary = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8}
    return dictionary.get(letter.lower(), -1)

def insert_ship(length, starting_pos, orientation, grid):
    """Attempt to insert a ship into the grid.
    Returns (status, new_grid, ship_coords).
    status: "success" or "error"
    ship_coords: set of (row, col) tuples occupied by the ship on success."""
    if len(starting_pos) < 2:
        return "error", grid, None
    col = letter_to_num(starting_pos[0])
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

def display_grid(grid, hide_ships=False):
    for row in grid:
        if hide_ships:
            print(" ".join(' ' if cell == 's' else cell for cell in row))
        else:
            print(" ".join(row))

def check_win(grid):
    for row in grid:
        if 's' in row:
            return False
    return True

def handle_hit(row, col, opponent_ships):
    """Remove the hit coordinate from the appropriate ship in opponent_ships.
    If a ship is completely destroyed, announce it."""
    for ship in opponent_ships:
        if (row, col) in ship:
            ship.remove((row, col))
            if len(ship) == 0:
                print("You have sunk a ship!")
                opponent_ships.remove(ship)
            break

def player_turn(player, own_grid, opponent_grid, opponent_ships):
    clear_screen()
    print(f"Player {player}'s Turn\n")
    print("Your grid:")
    display_grid(own_grid)
    print("\nOpponent's grid:")
    display_grid(opponent_grid, hide_ships=True)

    while True:
        guess = input("\nEnter your guess (e.g., a1, c3): ").strip().lower()
        if len(guess) < 2:
            print("Invalid format, try again.")
            continue

        col = letter_to_num(guess[0])
        try:
            row = int(guess[1])
        except ValueError:
            print("Invalid format, try again.")
            continue

        if 1 <= row <= 8 and 1 <= col <= 8:
            if opponent_grid[row][col] == "s":
                print("Hit!")
                opponent_grid[row][col] = "x"
                handle_hit(row, col, opponent_ships)
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

    input("\nPress Enter to continue...")

def two_player_mode():
    # Clear the screen and display ASCII art at the start
    clear_screen()
    print(r"""
  ____        _   _   _           _     _       
 |  _ \      | | | | | |         | |   (_)      
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                          | |    
                                          |_|    

          WELCOME TO TWO PLAYER MODE
    """)

    print("Instructions:")
    print("1. The grid is 8x8. Columns are labeled a-h, and rows are labeled 1-8.")
    print("2. You and your opponent will place 5 ships each:")
    print("   - 2 ships of length 2")
    print("   - 2 ships of length 3")
    print("   - 1 ship of length 4")
    print("3. To place a ship, you will be asked for a starting position (e.g., 'a1') ")
    print("   and an orientation ('n' for north/up, 's' for south/down, 'e' for east/right, 'w' for west/left).")
    print("4. Ships cannot overlap or be placed outside the grid.")
    print("5. On your turn, guess a cell (e.g., 'c5'). A hit will be marked with 'x', a miss with 'o'.")
    print("   If you sink all opponent ships, you win!")
    input("\nPress Enter to start the game...")

    # Define ship sizes for each player
    # 2 ships of length 2, 2 ships of length 3, 1 ship of length 4
    ship_sizes = [2, 2, 3, 3, 4]

    p1_grid = create_grid()
    p2_grid = create_grid()

    p1_ships = []
    p2_ships = []

    # Player 1 places ships
    clear_screen()
    print("Player 1, place your ships")
    for i, size in enumerate(ship_sizes, start=1):
        while True:
            display_grid(p1_grid)
            print(f"\nYou need to place a ship of length {size}.")
            start = input("Enter the starting position for this ship (e.g., a1): ").strip().lower()
            orient = input("Enter orientation (n, s, e, w): ").strip().lower()
            result, p1_grid, coords = insert_ship(size, start, orient, p1_grid)
            if result == "success":
                p1_ships.append(coords)
                break
            else:
                print("Invalid position or orientation. The ship was not placed. Try again.")

    clear_screen()

    # Player 2 places ships
    print("Player 2, place your ships")
    for i, size in enumerate(ship_sizes, start=1):
        while True:
            display_grid(p2_grid)
            print(f"\nYou need to place a ship of length {size}.")
            start = input("Enter the starting position for this ship (e.g., a1): ").strip().lower()
            orient = input("Enter orientation (n, s, e, w): ").strip().lower()
            result, p2_grid, coords = insert_ship(size, start, orient, p2_grid)
            if result == "success":
                p2_ships.append(coords)
                break
            else:
                print("Invalid position or orientation. The ship was not placed. Try again.")

    # Game loop
    while True:
        # Player 1's turn
        player_turn(1, p1_grid, p2_grid, p2_ships)
        if check_win(p2_grid):
            print("Player 1 wins!")
            break

        # Player 2's turn
        player_turn(2, p2_grid, p1_grid, p1_ships)
        if check_win(p1_grid):
            print("Player 2 wins!")
            break

    # After game ends, offer the option to retry or go back to menu
    while True:
        choice = input("\nGame Over! Would you like to (R)etry or go back to (M)enu?: ").strip().lower()
        if choice == 'r':
            return two_player_mode()
        elif choice == 'm':
            return "menu"
        else:
            print("Invalid choice. Please type 'r' or 'm'.")

