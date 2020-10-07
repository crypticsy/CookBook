import sys
sys.setrecursionlimit(10**6) 


grid,empty = [],[]
row,col,table = [{x:set() for x in range(9)} for x in range(3)]

def findemptycells():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                empty.append((x,y))
            else:
                row[x].add(grid[x][y])
                col[y].add(grid[x][y])
                a,b = x//3,y//3
                table[a*3+b].add(grid[x][y])


def solver(i=0, j=0, n=0):
    x,y = (-1,-1) if n>=len(empty) else empty[n]
    if x == -1:return True
        
    for z in range(1,10):
        temp = (x//3)*3+y//3
        if z not in row[x] and z not in col[y] and z not in table[temp]:
            row[x].add(z)
            col[y].add(z)
            table[temp].add(z)
            grid[x][y] = z

            if solver(x,y,n+1):return True
            
            row[x].remove(z)
            col[y].remove(z)
            table[temp].remove(z)
            grid[x][y] = 0
            
    return False 
    


#Testing

values = ['800000000', '003600000', '070090200', '050007000', '000045700', '000100030', '001000068', '008500010', '090000400'] # World's hardest sudoku problem
for i in values:
    grid.append([int(x) for x in i])

findemptycells()
solver()


[print(*x,sep="") for x in grid]


# Output:
#
# 812753649
# 943682175
# 675491283
# 154237896
# 369845721
# 287169534
# 521974368
# 438526917
# 796318452
#
# Run time : 0.117s
