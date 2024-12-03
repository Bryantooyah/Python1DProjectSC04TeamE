import copy


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

def letter_to_num(letter):
    dictionary = {'a' : 1,'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
    return dictionary[letter]

def insert_ship(length, starting_pos, orientation, grid): #starting_pos will be in the format a1, c5, etc | orientation will be in the format of n, s, e, w
    collumn = starting_pos[0]
    collunm = int(letter_to_num(collumn))
    row = int(starting_pos[1])
    original_grid = copy.deepcopy(grid)

    for i in range(length):

        if grid[row][collumn] == " ":
            grid[row][collumn] = 's'
        else:
            grid = original_grid
            return 'error! - No space remaining on the grid!'

        if orientation == 'n':
            row -= 1
        elif orientation == 's':
            row += 1
        elif orientation == 'e':
            collumn += 1
        elif orientation == 'w':
            collumn -= 1

    return grid

print(p1_grid5x5)
starting_pos = input('Enter starting_pos in the format a1, c3, d2, etc. \n')
orientation = input('Enter orientation in the format n, s, e, w \n')
p1_grid5x5 = insert_ship(3, starting_pos, orientation, p1_grid5x5)
print(p1_grid5x5)
