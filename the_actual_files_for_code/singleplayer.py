# import random
import time

# Constants for the game
GRID_SIZE = 8
LETTERS = ["x", "a", "b", "c", "d", "e", "f", "g", "h"]
SHIP_SIZES = [4, 3, 3, 2, 2]
SHIPS = ["Battleship (4)", "Cruiser (3)", "Cruiser (3)", "Gun Boat (2)", "Gun Boat (2)"]
HIT_POINTS = 5
SUNK_POINTS = 20
MISS_POINTS = -3
TIME_BONUS = 40
TIME_LIMIT = 300  # 5 minutes

# Initialize player score and game variables
player_score = 0
player_ships = []
computer_ships = []
player_grid = []
computer_grid = []
player_hit_miss_grid = []
computer_guesses = set()
game_start_time = 0

def create_grid():
    """Create an 8x8 grid."""
    grid = [[" " for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]
    grid[0] = ["x"] + ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(1, GRID_SIZE + 1):
        grid[i][0] = str(i)
    return grid

def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(" ".join(row))

def coordinate_to_index(coord):
    """Convert the coordinate (e.g., A1) to indices."""
    try:
        col = LETTERS.index(coord[0].lower())
        row = int(coord[1]) 
        if 1 <= col <= GRID_SIZE and 1 <= row <= GRID_SIZE:
            return row, col
    except (ValueError, IndexError):
        return None
    return None

def place_ship(grid, size, ship_name, is_player=True):
    """Place a ship on the grid."""
    if is_player:
        print(f"\nPlace your {ship_name} (Size {size})")
    while True:
        if is_player:
            print("\nCurrent Grid:")
            print_grid(grid)
            start = input(f"Enter the starting coordinate (e.g., A1): ").strip()
            direction = input("Enter direction ('n' for north, 's' for south, 'e' for east, 'w' for west): ").strip().lower()
            start_coord = coordinate_to_index(start)
        else:
            start_coord = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            direction = random.choice(['n', 's', 'e', 'w'])

        if start_coord is None:
            if is_player:
                print("Invalid coordinate. Please try again.")
            continue

        row, col = start_coord

        if direction == 'n' and row - size + 1 >= 0:
            if all(grid[row - i][col] == " " for i in range(size)):
                for i in range(size):
                    grid[row - i][col] = "S" if is_player else "C"
                return [(row - i, col) for i in range(size)]
        elif direction == 's' and row + size - 1 < GRID_SIZE:
            if all(grid[row + i][col] == " " for i in range(size)):
                for i in range(size):
                    grid[row + i][col] = "S" if is_player else "C"
                return [(row + i, col) for i in range(size)]
        elif direction == 'e' and col + size - 1 < GRID_SIZE:
            if all(grid[row][col + i] == " " for i in range(size)):
                for i in range(size):
                    grid[row][col + i] = "S" if is_player else "C"
                return [(row, col + i) for i in range(size)]
        elif direction == 'w' and col - size + 1 >= 0:
            if all(grid[row][col - i] == " " for i in range(size)):
                for i in range(size):
                    grid[row][col - i] = "S" if is_player else "C"
                return [(row, col - i) for i in range(size)]

        if is_player:
            print("Invalid placement. Please try again.")
        else:
            continue

def update_score(event, sunk=False):
    """Update the score."""
    global player_score
    if event == "hit":
        player_score += HIT_POINTS
    elif event == "miss":
        player_score += MISS_POINTS
    if sunk:
        player_score += SUNK_POINTS

def random_computer_guess():
    """Generate a random guess for the computer."""
    while True:
        guess = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if guess not in computer_guesses:
            computer_guesses.add(guess)
            return guess

def print_hit_miss_grid(grid):
    """Print player's hit/miss grid."""
    print("\nYour Attack Grid (Hits and Misses):")
    for row in grid:
        print(" ".join(row))

def play_game():
    """Main game function."""
    global player_score, player_ships, computer_ships, player_grid, computer_grid, game_start_time, player_hit_miss_grid

    print("Welcome to Battleship!")
    print("You will place 5 ships on your grid.")
    
    # Initialize grids
    player_grid = create_grid()
    computer_grid = create_grid()
    player_hit_miss_grid = create_grid()

    # Place ships for the player
    for i, ship_name in enumerate(SHIPS):
        size = SHIP_SIZES[i]
        player_ships.extend(place_ship(player_grid, size, ship_name))

    # Place ships for the computer
    for i, ship_name in enumerate(SHIPS):
        size = SHIP_SIZES[i]
        computer_ships.extend(place_ship(computer_grid, size, ship_name, is_player=False))

    # Game start time
    game_start_time = time.time()

    # Main game loop
    while True:
        print("\nYour Grid (Ship Placement Visible):")
        print_grid(player_grid)

        # Player's turn
        print("\nYour turn to attack!")
        guess = input("Enter your attack coordinate (e.g., A1 or 'quit' to exit): ").strip()
        if guess.lower() == "quit":
            print("You have quit the game.")
            break

        attack_coord = coordinate_to_index(guess)
        if attack_coord:
            row, col = attack_coord
            if computer_grid[row][col] == "C":
                print("Hit!")
                computer_grid[row][col] = "X"  # Mark hit
                player_hit_miss_grid[row][col] = "X"
                update_score("hit")
                computer_ships.remove((row, col))
                if not computer_ships:
                    print("You sunk all the computer's ships!")
                    break
            else:
                print("Miss!")
                computer_grid[row][col] = "O"  # Mark miss
                player_hit_miss_grid[row][col] = "O"
                update_score("miss")

        # Computer's turn
        print("\nComputer's turn!")
        comp_row, comp_col = random_computer_guess()
        if player_grid[comp_row][comp_col] == "S":
            print(f"Computer hit your ship at {LETTERS[comp_col]}{comp_row + 1}!")
            player_grid[comp_row][comp_col] = "X"
            player_ships.remove((comp_row, comp_col))
            if not player_ships:
                print("Computer sunk all your ships!")
                break
        else:
            print(f"Computer missed at {LETTERS[comp_col]}{comp_row + 1}.")
            player_grid[comp_row][comp_col] = "O"

        # Print hit/miss grid
        print_hit_miss_grid(player_hit_miss_grid)
        
        print(f"\nCurrent score: {player_score}")

    # Game over, display final score and time
    total_time = time.time() - game_start_time
    print(f"\nGame over! Your final score: {player_score}")
    print(f"Time taken: {total_time:.2f} seconds")
    if not computer_ships:
        print("Congratulations! You win!")
    else:
        print("Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_game()
