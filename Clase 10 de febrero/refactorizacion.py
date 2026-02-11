# Update of first exercise.

## ----- Array Unidimencional ----- ##

# 1. create a list with five elements.
colors: list = ['Amarillo', 'Azul', 'Rojo', 'Verde', 'Morado']

# 2. get and print second element.
def get_element_index_1(my_list: list):
    return my_list[1]

print(get_element_index_1(colors))

# 3. insert the value: "Estructura de datos" in 3 position.
def insert_new_value(my_list: list, new_value: str, position: int):
    if not 0 <= position <= len(my_list):
        return None
    else:
        my_list.insert(position, new_value)
        return my_list
    
print(insert_new_value(colors, "Estructura de datos", 2))
    
# 4. Search for the value: "Estructura de datos" and return your index. 
def search_value(my_list: list, value: str):
    for index, item in enumerate(my_list):
        if item == value:
            return index
    return None

print(search_value(colors, 'Estructura de datos'))

## ----- Array Bidimensional ----- ##

# 1. Create a 2D array with 3 rows and 3 columns.
ages: list = [[15,25,33],
            [45,28,36],
            [36,55,87]]

# 2. get and print the element of the position [1][1]
def get_element_index_2(my_list: list, row: int, col: int):
    if not 0 <= row < len(my_list) or not 0 <= col < len(my_list[row]):
        return None
    else:
        return my_list[row][col]

print(get_element_index_2(ages, 1, 1))

# 3. Delete of the element in the position [2][2]
def delete_element(my_list: list, row: int, col:int):
    if not 0 <= row < len(my_list) or not 0 <= col < len(my_list[row]):
        return None
    else:
        my_list[row].pop(col)
        return my_list
    
print(delete_element(ages, 2, 2))