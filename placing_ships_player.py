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
while int(row_select) < 1 or int(row_select) > 5:
    row_select = input("Choose a different row to place the ship.")
column_select = input("Choose a column to place the ship.")
while int(column_select) < 1 or int(column_select) > 5:
    column_select = input("Choose a different column to place the ship.")

# Choosing Final Piece

final_row_select = input("Choose a row to finish the ship.")
while int(final_row_select) < 1 or int(final_row_select) > 5:
    final_row_select = input("Choose a different row to finish the ship.")
while abs(int(row_select) - int(final_row_select)) > 4:
    final_row_select = input("Choose a different row to finish the ship.")
final_column_select = input("Choose a column to finish the ship.")
while int(final_column_select) < 1 or int(final_column_select) > 5:
    final_column_select = input("Choose a different column to finish the ship.")
while abs(int(column_select) - int(final_column_select)) > 4:
    final_column_select = input("Choose a different column to finish the ship.")

# Placing the ship

def ship_placing(a,b):
    ship_length = 0
    if int(final_row_select) > int(row_select) and int(final_column_select) == int(column_select):
        for i in range(int(row_select),int(final_row_select)+1):
            row = str(i)
            column = int(final_column_select) - 1
            empty_grid5x5[row][column] = 'X'
            ship_length += 1
    if int(final_row_select) < int(row_select) and int(final_column_select) == int(column_select):
        for i in range(int(final_row_select),int(row_select)+1):
            row = str(i)
            column = int(final_column_select) - 1
            empty_grid5x5[row][column] = 'X'
            ship_length += 1
    if int(column_select) < int(final_column_select) and int(final_row_select) == int(row_select):
        for i in range(int(column_select) - 1,int(final_column_select)):
            column = i
            row = a
            empty_grid5x5[row][column] = 'X'
            ship_length += 1
    if int(column_select) > int(final_column_select) and int(final_row_select) == int(row_select):
        for i in range(int(final_column_select) - 1,int(column_select)):
            column = i
            row = a
            empty_grid5x5[row][column] = 'X'
            ship_length += 1
    return empty_grid5x5

# Printing the Ship

placed_grid = ship_placing(final_row_select,final_column_select)
for i in placed_grid:
    print(empty_grid5x5[i])