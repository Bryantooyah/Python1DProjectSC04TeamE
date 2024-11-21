# Python1DProjectSC04TeamE

Game: Battle Ship

Team Members:
Bryan Chua Bing Huan - 1008743
Pang Jie, Maximus - 1009198 Single Player AI
Khoo Jing Xuan - 1008974 Title Screen, Setting, Quit, 2 Player
Davin Handreas Chen - 1009595 High Score, End Game
Brandon Cheang Ming Wei - 1008839 assign ships to the board, Single Player
Sanjan Krishna Sarat - 1009153 2 Player

Hello I am Sanjan and I am testing hehehe

Features:
Title Screen:
    - Single player
    - 2 player
    - High Score
    - (Gear Icon) Settings
    - quit game

Setting: 
Sound (Master Volume, Game Volume, Music Volume)
Username 
History Log (Points, Past Game wins and losses, Win %)

HighScore:
HighScore is based on points, time

Quit Game:
Terminate the code

Single Player:

Feature in Single Player AI 
Generation: Randomly assign the ship on the board ensure that no two ship overlaps and does not exceed board area.
Attack Process: (random at start, once ship is hit, it will only randomly generate the 4 squares around to hit, once a whole ship is gone, randomly select other parts of the board)

Board Sizes (5 x 5 - 8 x 8)

Number of Ships,boardsize remain the same: 1 * 4 wide ship , 2 * 3 wide ship, 2 * 2 wide ship
 
Time Limit each round (randomly attack somewhere on the board) {15 Seconds - 60 Seconds}

GamePlay:
Assign the Ships to the board:
    Choose which Ship to Place on the Board
    Ensure the Ships wont overlap
    Ships not placed diagonally
    Place Ship (Adding Cross to the board{flickering cross to show where the ship was placed}, checking if straight or down)
    Confirm Button
Playing:
    Count down timer at the bottom
    Click on the board squares for where to attack
    New turn allocated to player once they hit.
    At the bottom right corner place a (mini board of your own board {we can see our own ships and where the enemy has guessed})
After Game: 
    Algorithm to check that all ship are dead.
    Calculate Point System
        Time (Length of the game{when start of first person})
        Calculate Score Based:
            Every Ship Destroyed (+20 Points)
            Every Hit (+5 Points)
            Miss (-2 Points)
    Add to leaderboard
    Move Back to Title Screen

2 Player:
Pass to Play System

Board Sizes (5 x 5 - 8 x 8)

Number of Ships of each boardsize remain the same: 1 * 4 wide ship , 2 * 3 wide ship, 2 * 2 wide ship
 
Time Limit each round (randomly attack somewhere on the board) {15 Seconds - 60 Seconds}

Input UserName for Player 2

GamePlay:
Assign the Ships to the board:
    Choose which Ship to Place on the Board
    Ensure the Ships wont overlap
    Place Ship (Adding Cross to the board{flickering cross to show where the ship was placed}, checking if straight or down)
    Confirm Button
Repeat for Player 2

Playing:
    Count down timer at the bottom
    Click on the board squares for where to attack
    New turn allocated to player once they hit.
    At the bottom right corner place a (mini board of your own board {we can see our own ships and where the enemy has guessed})
Repeat for Player 2

After Game: 
    Algorithm to check that all ship are dead.
    Say who won
    Move Back to Title Screen

Example of how we should code:
## EGs
# import turtle as tur

# tur.speed(0)

# ### Draw a square (inputs: none)
# def draw_square():
#     for i in range(4):
#         tur.forward(100)
#         tur.right(90) 
# draw_square()
##




