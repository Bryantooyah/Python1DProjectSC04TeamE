#This is just a 5x5 grid that will be initialized at the start of each game
#o (not 0) means miss and x means a hit

p1_grid5x5 = [
    ["x","a","b","c","d","e"],
    ["1"," "," "," "," "," "],
    ["2"," "," "," "," "," "],
    ["3"," "," "," "," "," "],
    ["4"," "," "," "," "," "],
    ["5"," "," "," "," "," "],
]

p2_grid5x5 = [
    ["x","a","b","c","d","e"],
    ["1"," "," "," "," "," "],
    ["2"," "," "," "," "," "],
    ["3"," "," "," "," "," "],
    ["4"," "," "," "," "," "],
    ["5"," "," "," "," "," "],
]

def letter_to_num(a):
    dictionary = {'a' : 1,'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
    return didctionary[a]

def insert_ship(length, starting_pos, orientation): #starting_pos will be in the format a1, c5, etc
    collumn = starting_pos[0]
    collunm = letter_to_num(collumn) 
    row = starting_pos[1]

    for i in range(length):

