
# Making grid with empty spaces

empty_grid5x5 = {
    '1': ["","","","",""],
    '2': ["","","","",""],
    '3': ["","","","",""],
    '4': ["","","","",""],
    '5': ["","","","",""]
}

# Making player choose initial square
row_select = input("Choose a row to place the ship.")  
column_select = input("Choose a column to place the ship.")

# Placing the initial piece

def grid_select(a,b):
    row = str(a)
    column = int(b) - 1
    empty_grid5x5[row][column] = 'X'
    return empty_grid5x5

placed_grid = grid_select(row_select,column_select)

# Choosing orientation to finish the ship 

direction = input("Choose a direction to place the ship") # For now use NSEW, can decide on this later
while direction.isalpha() == False:
    direction = input("Please choose North, South, East or West")
direction = direction.title()