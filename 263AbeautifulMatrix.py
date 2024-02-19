matrix = []
for k in range(5):
    matrix.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row , col = i , j

moves = abs(row - 2) + abs(col - 2)
print(moves)
