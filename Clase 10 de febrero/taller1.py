# First exercise 

# Create a list with 5 elements
colors: list = ['Amarillo', 'Azul', 'Rojo', 'Verde', 'Morado']
print(colors[1]) # 
colors.insert(2, "Estructura de datos")

for index, color in enumerate(colors):
    if color == "Estructura de datos":
        print(index)


# Create a list 3x3.
ages: list = [[15,25,33],
            [45,28,36],
            [36,55,87]]

print(ages[1][1])
del ages[2][2]

for index, age in enumerate(ages):
    for index2, age2 in enumerate(ages[index]):
        if age2 == 28:
            print(f"{index},{index2}")