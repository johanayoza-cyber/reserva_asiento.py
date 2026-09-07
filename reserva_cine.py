asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))
asientos[fila][columna] = 1

print("Estado de la sala:")
for i in range(0, 3):
    for j in range(0, 4):
        print(asientos[i][j], end=" ")
    print()