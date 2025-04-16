# Tugas Matriks 5X5
A = [ 
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [3, 4, 5, 1, 2],
    [4, 5, 1, 2, 3],
    [5, 1, 2, 3, 4]
]

B = [
    [5, 4, 3, 2, 1],
    [4, 3, 2, 1, 5],
    [3, 2, 1, 4, 5],
    [2, 1, 3, 4, 5],
    [1, 5, 4, 3, 2]
]

n = 5
C = []
for a in range(n):
    row = []
    for b in range(n):
        element = 0
        for c in range(n):
            element += A[a][c] * B[c][b]
        row.append(element)
    C.append(row)

for row in C:
    print(row)
