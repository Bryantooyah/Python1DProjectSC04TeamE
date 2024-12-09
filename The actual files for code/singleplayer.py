import time
import random

# Constants
GRID_SIZE = 8
GRID_TEMPLATE = [
    ["x", "a", "b", "c", "d", "e", "f", "g", "h"],
    ["1", " ", " ", " ", " ", " ", " ", " ", " "],
    ["2", " ", " ", " ", " ", " ", " ", " ", " "],
    ["3", " ", " ", " ", " ", " ", " ", " ", " "],
    ["4", " ", " ", " ", " ", " ", " ", " ", " "],
    ["5", " ", " ", " ", " ", " ", " ", " ", " "],
    ["6", " ", " ", " ", " ", " ", " ", " ", " "],
    ["7", " ", " ", " ", " ", " ", " ", " ", " "],
    ["8", " ", " ", " ", " ", " ", " ", " ", " "],
]
SHIP_TYPES = {"Battleship": 4, "Cruiser": 3, "Gun boat": 2}
SHIP_COUNTS = {"Battleship": 1, "Cruiser": 2, "Gun boat": 2}
SCORE_HIT = 5
SCORE_SUNK = 20
SCORE_MISS = -3

def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(" ".join(row))

def coordinate_to_index(coord):
    """Convert a coordinate like 'a1' to grid indices."""
    try:
        col = GRID_TEMPLATE[0].index(coord[0].lower())
        row = int(coord[1])
        return row, col
    except (ValueError, IndexError):
        return None

def is_valid_ship_placement(grid, row, col, size, orientation):
    """Check if the ship placement is valid."""
    if orientation == "n":
        if row - size + 1 < 1:
            return False
        return all(grid[row - i][col] == " " for i in range(size))
    elif orientation == "s":
        if row + size - 1 > GRID_SIZE:
            return False
        return all(grid[row + i][col] == " " for i in range(size))
    elif orientation == "e":
        if col + size - 1 > GRID_SIZE:
            return False
        return all(grid[row][col + i] == " " for i in range(size))
    elif orientation == "w":
        if col - size + 1 < 1:
            return False
        return all(grid[row][col - i] == " " for i in range(size))
    return False

def place_ship(grid, row, col, size, orientation):
    """Place a ship on the grid."""
    ship_coordinates = []
    if orientation == "n":
        for i in range(size):
            grid[row - i][col] = "S"
            ship_coordinates.append((row - i, col))
    elif orientation == "s":
        for i in range(size):
            grid[row + i][col] = "S"
            ship_coordinates.append((row + i, col))
    elif orientation == "e":
        for i in range(size):
            grid[row][col + i] = "S"
            ship_coordinates.append((row, col + i))
    elif orientation == "w":
        for i in range(size):
            grid[row][col - i] = "S"
            ship_coordinates.append((row, col - i))
    return ship_coordinates

def place_computer_ships(grid):
    """Place computer ships randomly."""
    computer_ships = []
    for ship, size in SHIP_TYPES.items():
        for _ in range(SHIP_COUNTS[ship]):
            while True:
                orientation = random.choice(["n", "s", "e", "w"])
                row = random.randint(1, GRID_SIZE)
                col = random.randint(1, GRID_SIZE)
                if is_valid_ship_placement(grid, row, col, size, orientation):
                    computer_ships.extend(place_ship(grid, row, col, size, orientation))
                    break
    return computer_ships

def get_player_placement(grid, ship_name, size):
    """Let the player place a ship."""
    print(f"Place your {ship_name} of size {size}.")
    while True:
        try:
            start_coord = input("Enter the starting coordinate (e.g., a1): ").strip().lower()
            orientation = input("Enter orientation ('n', 's', 'e', 'w'): ").strip().lower()
            indices = coordinate_to_index(start_coord)
            if indices:
                row, col = indices
                if is_valid_ship_placement(grid, row, col, size, orientation):
                    return place_ship(grid, row, col, size, orientation)
            print("Invalid placement. Try again.")
        except Exception:
            print("Error in input. Try again.")

def calculate_score(score, event, ship_sunk=False):
    """Update the score based on the event."""
    if event == "hit":
        score += SCORE_HIT
    elif event == "miss":
        score += SCORE_MISS
    if ship_sunk:
        score += SCORE_SUNK
    return score

def play_game():
    """Main function to play the game."""
    player_grid = [row[:] for row in GRID_TEMPLATE]
    computer_grid = [row[:] for row in GRID_TEMPLATE]
    player_score = 0
    player_ships = []
    computer_ships = []

    print("Welcome to Battleship!")
    print("Your initial grid:")
    print_grid(player_grid)

    # Place player ships
    for ship, size in SHIP_TYPES.items():
        for _ in range(SHIP_COUNTS[ship]):
            player_ships.extend(get_player_placement(player_grid, ship, size))
            print("Your updated grid:")
            print_grid(player_grid)

    # Place computer ships
    computer_ships = place_computer_ships(computer_grid)

    print("\nLet the game begin!")
    start_time = time.time()

    while True:
        # Show player's grid
        print("\nYour grid:")
        print_grid(player_grid)
        print(f"Your score: {player_score}")

        # Player's turn
        guess = input("Enter your guess (e.g., a1) or type 'quit' to exit: ").strip().lower()
        if guess == "quit":
            print("You quit the game.")
            break
        indices = coordinate_to_index(guess)
        if indices:
            row, col = indices
            if computer_grid[row][col] == "S":
                print("Hit!")
                computer_grid[row][col] = "X"
                player_score = calculate_score(player_score, "hit")
                computer_ships.remove((row, col))
                if all(computer_grid[r][c] == "X" for r, c in computer_ships if (r, c) in computer_ships):
                    player_score = calculate_score(player_score, "hit", ship_sunk=True)
            else:
                print("Miss!")
                computer_grid[row][col] = "O"
                player_score = calculate_score(player_score, "miss")

        # Check if all computer ships are sunk
        if not computer_ships:
            print("Congratulations! You sank all the computer's ships!")
            break

    # End game
    end_time = time.time()
    game_duration = end_time - start_time
    print("\nFinal score:", player_score)
    print("Time taken:", round(game_duration, 2), "seconds")
    print("Thanks for playing Battleship!")

# Run the game
play_game()