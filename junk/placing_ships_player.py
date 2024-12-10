p1_grid5x5 = [
    ["x","a","b","c","d","e"],
    ["1"," "," "," "," "," "],
    ["2"," "," "," "," "," "],
    ["3"," "," "," "," "," "],
    ["4"," "," "," "," "," "],
    ["5"," "," "," "," "," "],]

horizontal_select = {"a":1, "b":2, "c":3, "d":4, "e":5}

def safety_checks(square):
    # Making sure there is only one number and one letter

    numbers = 0
    letters = 0
    while letters == 0 or numbers == 0:
        for i in range(len(square)):
            if square[i].isnumeric():
                numbers += 1
            elif square[i].isalpha():
                letters += 1
        if numbers != 1 or letters != 1:
            square = input('Choose a proper square: ')
            numbers = 0
            letters = 0

    # Making sure it is within the grid

    tester = 0
    overlap_tester = 0

    while tester < 2:
        for i in range(len(square)):
            if square[i].isnumeric() and 0 < int(square[i]) < 6:
                tester += 1
            elif square[i].isalpha() and square[i] in horizontal_select.keys():
                tester += 1
            else:
                square = input('Choose a proper square: ')
                tester = 0

    for i in range(len(square)):
        if square[i].isalpha() == True:
            column = horizontal_select[square[i]]
        elif square[i].isdigit() == True:
            row = int(square[i])
    return row, column

def direction_check(direction,row,column,length):
    checker = 0
    while checker == 0:
        if direction == 'NORTH' and row - length < 0:
            direction = input('Choose a different direction: ').upper()
        elif direction == 'SOUTH' and row + length > 6:
            direction = input('Choose a different direction: ').upper()
        elif direction == 'EAST' and column + length > 6:
            direction = input('Choose a different direction: ').upper()
        elif direction == 'WEST' and column - length < 0:
            direction = input('Choose a different direction: ').upper()
        else:
            checker += 1
    return direction

def placing_ship(length):
    row, column = 0, 0

    # Choosing the first square

    square = input('Choose a square: ').lower()

    row, column = safety_checks(square)[0],safety_checks(square)[1]

    while p1_grid5x5[row][column] == 'X':
        square = input('Choose a different square: ').lower()
        row,column = safety_checks(square)[0],safety_checks(square)[1]

    p1_grid5x5[row][column] = "X"

    # NSEW?

    direction = input('Place the ship North, South, East or West')
    direction = direction.upper()
    directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

    while direction not in directions:
        direction = input('Choose a different direction: ').upper()

    direction = direction_check(direction,row,column,length)

    if direction == "NORTH":
        for i in range(length-1):
            row = row - 1
            p1_grid5x5[row][column] = 'X'
    if direction == "SOUTH":
        for i in range(length-1):
            row = row + 1
            p1_grid5x5[row][column] = 'X'
    if direction == "EAST":
        for i in range(length-1):
            column = column + 1
            p1_grid5x5[row][column] = 'X'
    if direction == "WEST":
        for i in range(length-1):
            column = column - 1
            p1_grid5x5[row][column] = 'X'
    return p1_grid5x5

placed_grid = placing_ship(3)
placed_grid = placing_ship(3)
for i in placed_grid:
    print(i)