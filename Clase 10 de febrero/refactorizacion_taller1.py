# Update of first exercise.

## ----- Array Unidimensional ----- ##

# 1. Create a list with five elements.
colors: list = ['Amarillo', 'Azul', 'Rojo', 'Verde', 'Morado']

# 2. Get and print the second element.
def get_second_element(my_list: list):
    return my_list[1]

print("Second element: ", get_second_element(colors))

# 3. Insert the value: "Estructura de datos" at 3 position.
def insert_new_value(my_list: list, new_value: str, position: int):
    if not 0 <= position <= len(my_list):
        return None
    else:
        my_list.insert(position, new_value)
        return my_list
    
print("List updated with the new element: ",insert_new_value(colors, "Estructura de datos", 2))
    
# 4. Search for the value: "Estructura de datos" and return your index. 
def search_value(my_list: list, value: str):
    for index, item in enumerate(my_list):
        if item == value:
            return index
    return None

print("Index of element 'Estructura de datos': ", search_value(colors, 'Estructura de datos'))

## ----- Array Bidimensional ----- ##

# 1. Create a 2D array with 3 rows and 3 columns.
ages: list[list[int]] = [[15,25,33],
            [45,28,36],
            [36,55,87]]

# 2. Get and print the element of the position [1][1]
def get_element(my_list: list, row: int, col: int):
    if not 0 <= row < len(my_list) or not 0 <= col < len(my_list[row]):
        return None
    else:
        return my_list[row][col]

print("Element at row 2 and column 2: ",get_element(ages, 1, 1))

# 3. Delete the element at position [2][2]
def delete_element(my_list: list, row: int, col:int):
    if not 0 <= row < len(my_list) or not 0 <= col < len(my_list[row]):
        return None
    else:
        my_list[row].pop(col)
        return my_list
    
print("List updated after deleting element in row 3, column 3: ",delete_element(ages, 2, 2))

# 4. Search for a value in row 2 and return its index.
def search_value_in_row(my_list: list, row: int, value: int):
    if not 0 <= row < len(my_list):
        return None
    else:
        for index, item in enumerate(my_list[row]):
            if item == value:
                return row, index
    return None

print("Index of element with value 28 in row 2: ",search_value_in_row(ages, 1, 28))