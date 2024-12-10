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
{Provide longer explanation with what is in it}
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

2 Player:
1. create_grid
- initiates the grid for game
2. letter_to_num
- changes the column from alphabert to number
3. insert_ship
- player places a ship within the grid coordinates (e.g. A1) and that will be the starting point. After that the player must decide the orientation of the ship using North(n), South(s), East(e) and West(w). This will be where the rest of the ship will be in relation to the starting point.
4. handle_hit
- Remove the hit coordinate from the appropriate ship in opponent_ships. If a ship is completely destroyed, announce it.
5. player_turn
- handles the attacking of oponent ships
6. print_you_win
- 

High Score:
{Provide longer explanation with what is in it}

Settings:
Contain the followig functions:
    - TitleScreen (Display "BattleShip" ASCII)
    - Options (Allow user choose the options "Singleplayer"/"2Player"/"Highscore"/"Setting"/"Quit")
    - Setting (Allow user to Change Username, view history log or go back title screen)
