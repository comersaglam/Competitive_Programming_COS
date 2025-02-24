# Practice makes it perfect
# inzva community built algoleague for every algorithm enthusiast hungry 
# for self-improvement and friendly competition. Have fun and good luck!
import copy

def checkneighbours(matrix, check, nrow, ncol):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
    for nb in directions:
        if (nrow + nb[0]) >= 0 and (nrow + nb[0]) < len(matrix):
            if (ncol + nb[1]) >= 0 and (ncol + nb[1]) < len(matrix[0]):
                if matrix[nrow + nb[0]][ncol + nb[1]] == check:
                    return True
    return False


datalist = []
inp_row, inp_col = map(int, input().strip().split(" "))
for i in range(inp_row):
    rowlist = []
    rowlist = [int(item) for item in input().split()]
    datalist.append(rowlist)

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
datalist2 = copy.deepcopy(datalist)

for nrow, row in enumerate(datalist):
    for ncol, elem in enumerate(row):
        if elem == 23:
            if not checkneighbours(datalist, 23, nrow, ncol):
                datalist2[nrow][ncol] = 35
        elif elem == 35:
            if not checkneighbours(datalist, 35, nrow, ncol):
                datalist2[nrow][ncol] = 23

for row in datalist2:
    print(*row)


