matrix = []
for i in range(5):
    row = input().split()
    matrix.append(row)

def updateMatrix(x,y,val):
    matrix[y][x] = val

for y1 in matrix:
    for x1 in matrix[matrix.index(y1)]:
        if matrix[matrix[matrix.index(y1)].index(x1)][matrix.index(y1)] == "1":
            print(matrix[matrix.index(y1)].index(x1), matrix.index(y1))

# for c in matrix:
#     print(c)