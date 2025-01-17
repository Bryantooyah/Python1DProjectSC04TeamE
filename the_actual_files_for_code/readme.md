Game: BattleShips

Team Members:
Bryan Chua Bing Huan - 1008743
Pang Jie, Maximus - 1009198 
Khoo Jing Xuan - 1008974 
Davin Handreas Chen - 1009595 
Brandon Cheang Ming Wei - 1008839 
Sanjan Krishna Sarat - 1009153 


Files included: 
main.py
menu.py
singleplayer.py
two_player.py
highscore.py
high_score.csv

To run:
1) Ensure the above files are included
2) Run main.py to begin playing the game

Reasons to use the program:
1) Battleship is a fun game!
2) They would like destress!

Features:

Users are prompted to key in an username before entering into the title screen.

Title Screen:
    - Single player {Challenge yourself and play against a computer bot}
    - 2 player {Pass and Play feature where you compete against a friend in a game of battleships}
    - High Score {View best score amongst all uers in single player mode}
    - Settings {Change username and view history log of your past games}
    - Quit game {Quits the game}

Single Player:
1) create_grid
- makes the grid for player and computer.
2) coord_to_index
- Linking the grid coordinates to have one letter and one number within the stipulated 8x8 created above.
3) place_ship
- the player places a ship within the grid coordinates    (e.g. A1) and that will be the starting point. After that the player must decide the orientation of the ship using North(n), South(s), East(e) and West(w). This will be where the rest of the ship will be in relation to the starting point.
4) update_score
- As the game progresses, hits, misses and ships sunk will be registered and updated as points. (Hit = 5 points, Ship sunk = 20 points and Misses = -3 points)
5) check_ship_sunk
- this code firstly registers all the grids that one ship occupies. As every time a ship is hit the grid will change from a 'S' to a 'X', Once all the grids of one ship has been replaced with a 'X', the ship is sunk. Afterwhich it will determine if the board which has the ship sunk belongs to 'Player' or 'Computer'.
6) attack_position
- Processes the attack made by the Computer and Player and updates it on the relevant grids and scores.
7) random_computer_guess
- Generates a random guess for the computer on the players grid.
8) print_hit_miss_grid
- Shows the player what grid he/she has hit on the computers(opponent's) board.
9) play_game
- The main game function that includes the following:
    - Introduction to the game
    - Instructions to the player to place the ships while updating the grids as the player places them.
    - As game starts, a timer starts at the background
    - When it is the players turn to attack, the code will prompt the player to do so while registering from the codes above on how many ship grids 'S' are left. If none are left, the game will end. This logic is also true for the computer. 
    - When the game ends, the code will display the score attined by the player and the duration of the game. If the player won against the computer, the code will congratulate the player. However if the player lost, the code will say "better luck next time". 

----------------

2 Player (Some functions like print_you_win have not been given as it is self explanatory):
1. create_grid
- Initiates the grid for game

2. letter_to_num
- Changes the column from alphabet to number

3. insert_ship
- Player places a ship within the grid coordinates (e.g. A1) and that will be the starting point. After that the player must decide the orientation of the ship using North(n), South(s), East(e) and West(w). This will be where the rest of the ship will be in relation to the starting point.

4. handle_hit
- Remove the hit coordinate from the appropriate ship in opponent_ships. If a ship is completely destroyed, announce it.

5. player_turn
- Handles the attacking of opponent ships

6. run
- This function compiles all the functions given above and runs the game. 

-----------------

High Score:
The HighScore class is designed to manage and display high scores for a game, handling tasks such as saving, loading, filtering, sorting, and displaying scores. The class initializes with a default file, high_score.csv, where all score records are stored. 

There are 4 main functions within this class, which includes: 
1. save_score: Append new score entries to the csv file, including the player's username, score, time taken (rounded to the nearest integer), game mode ("singleplayer" or "twoplayer"), and the game's status ("Win" or "Loss"). 

2. load_high_score: Reads the CSV file, filtering records where the condition is a "Win." If a player appears multiple times in the file, this function evaluates their best record based on the highest score and, in case of ties, the shortest time. Only the best record for each user is retained in the list of high scores.

3. sort_high_scores: This function takes in the list of high scores, process specifically for single-player mode, and sort the records in descending order of score. If scores are tied, it sorts them in ascending order of time taken. It returns the top 10 scores after sorting. 

4. display_high_score: This function prints the top 10 single-player high scores when called, including the rank, username, score, time, and the date and time when the score was achieved.

-----------------

Settings:
Contain the followig functions:
    - TitleScreen (Display "BattleShip" ASCII)
    - Options (Allow user choose the options "Singleplayer"/"2Player"/"Highscore"/"Setting"/"Quit")
    - Setting (Allow user to Change Username, view history log or go back title screen)
