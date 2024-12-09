import random
import time

class main(object):
    def __init__(self, context):
        self.__context = context

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


        def check_ship_sunk(ship_coordinates, grid, is_player):
            """
            Check if all parts of a ship have been hit.
            """
            for row, col in ship_coordinates:
                if grid[row][col] != "X":  # Check if any part of the ship is not hit
                    return False
            ship_owner = "Player's" if is_player else "Computer's"
            print(f"\n{ship_owner} Ship Sunk!")
            return True


        def attack_position(attacker, defender_grid, defender_ships, defender_hit_miss_grid, is_player_turn):
            """
            Process an attack and update the relevant grids and scores.
            """
            global player_score
            if is_player_turn:
                print("\nYour Hit/Miss Grid:")
                print_grid(defender_hit_miss_grid)
                guess = input("Enter a position to attack (e.g., A1): ").strip()
                guess_coord = coordinate_to_index(guess)
                if guess_coord is None:
                    print("Invalid coordinate. Try again.")
                    return False
            else:
                guess_coord = random_computer_guess()

            row, col = guess_coord
            if defender_grid[row][col] == "C" or defender_grid[row][col] == "S":
                print(f"\n{attacker} hits!")
                defender_grid[row][col] = "X"
                defender_hit_miss_grid[row][col] = "X"
                update_score("hit")

                # Check if any ship is sunk
                for ship_coordinates in defender_ships:
                    if (row, col) in ship_coordinates:
                        if check_ship_sunk(ship_coordinates, defender_grid, not is_player_turn):
                            defender_ships.remove(ship_coordinates)  # Remove the sunk ship
                            update_score("hit", sunk=True)
                        break
            elif defender_grid[row][col] == " ":
                print(f"\n{attacker} misses.")
                defender_grid[row][col] = "O"
                defender_hit_miss_grid[row][col] = "O"
                update_score("miss")
            else:
                if is_player_turn:
                    print("You've already attacked this position. Try again.")
                return False

            return True


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
                player_ships.append(place_ship(player_grid, size, ship_name))

            # Place ships for the computer
            for i, ship_name in enumerate(SHIPS):
                size = SHIP_SIZES[i]
                computer_ships.append(place_ship(computer_grid, size, ship_name, is_player=False))

            game_start_time = time.time()

            # Main game loop
            while True:
                print("\nYour Grid (Ship Placement Visible):")
                print_grid(player_grid)

                print("\nYour turn to attack!")
                if attack_position("Player", computer_grid, computer_ships, player_hit_miss_grid, is_player_turn=True):
                    if not computer_ships:
                        print("You sunk all the computer's ships! You win!")
                        break

                print("\nComputer's turn!")
                if attack_position("Computer", player_grid, player_ships, player_grid, is_player_turn=False):
                    if not player_ships:
                        print("Computer sunk all your ships! You lose!")
                        break

                print(f"\nCurrent score: {player_score}")

            # Game over, display final score and time
            total_time = time.time() - game_start_time
            print(f"\nGame over! Your final score: {player_score}")
            print(f"Time taken: {total_time:.2f} seconds")
            if not computer_ships:
                print("Congratulations! You win!")
            else:
                print("Better luck next time!")

        if __name__ == "__main__":
            play_game()

# After game ends, offer the option to retry or go back to menu
#        while True:
 #           choice = input("\nGame Over! Would you like to (R)etry or go back to (M)enu?: ").strip().lower()
  #          if choice == 'r':
   #             return "retry"
    #        elif choice == 'm':
     #           return "menu"
      #      else:
       #         print("Invalid choice. Please type 'r' or 'm'.")