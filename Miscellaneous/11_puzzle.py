# You are given the initial state of the board and you must output a list of moves to rearrange the tiles.

# Each tile is numbered from 1 to 11 (0 is the empty space). The final state is the following:

# 0  1  2  3
# 4  5  6  7
# 8  9 10 11
# In order to make a move, you need to print the coordinate of the tile you wish to move and it will take the place of the empty space. 
# The coordinate of a tile is the couple (row, column), with (0, 0) the top-left element.



import sys

goalPos = {" 0" : (0,0), " 1" : (1,0), " 2" : (2,0), " 3" : (3,0), " 4" : (0,1), " 5" : (1,1), " 6" : (2,1), " 7" : (3,1), " 8" : (0,2), " 9" : (1,2), "10" : (2,2), "11" : (3,2)}
goalboard = " 0 1 2 3 4 5 6 7 8 91011"          # input final goal state
board = ""  
movable = None

for i in range(3):
    for j,val in enumerate(input().split()):
        if val == "0":movable = (j,i)
        board += val.rjust(2)

print(board, file = sys.stderr)
print(movable, file = sys.stderr)


def generate(board, e_loc, new_loc):        # generate a new board by swaping the empy tile and the next tile
    empty, other = (4*e_loc[1] + e_loc[0])*2 , (4*new_loc[1] + new_loc[0])*2
    tile = board[other:other+2]
    board = board[:empty]+tile+board[empty+2:]
    board = board[:other]+" 0"+board[other+2:]
    return board


def findCost(board, n):
    cost = n
    for j in range(12):
        i,temp = j%4, (4*(j//4) + j%4)*2
        tile = board[temp:temp+2]
        if tile != " 0" and goalPos[tile] != (i,j//4):
            cost += abs((goalPos[tile][0] - i))+abs((goalPos[tile][1] - j//4))    # manhattan distance
    return cost


seen = set([board])
queue = {0:{"board":board, "movable":movable}}
path = {board:[]}
allcost = {board:findCost(board,0)}
found = False
counter = 1


def findMinKey():       # find the key of the move with least cost
    minkey, minval = -1, float('inf')
    for i in queue.keys():
        if allcost[queue[i]['board']] < minval and len(path[queue[i]['board']])<50:
            minkey, minval = i, allcost[queue[i]['board']]
    return minkey


while len(queue)>0:
    curkey = findMinKey()
    current = queue[curkey]
    curboard, cur_e_loc, curpath = current["board"], current["movable"], path[current["board"]]
    queue.pop(curkey)

    for i in [(0,1),(0,-1),(1,0),(-1,0)]:
        tx,ty = cur_e_loc[0]+i[0], cur_e_loc[1]+i[1]
        if tx >-1 and ty>-1 and tx<4 and ty<3:    
            newboard = generate(curboard, cur_e_loc,(tx,ty)) 
            if newboard not in seen:
                counter+=1
                queue[counter] = {"board" : newboard, "movable":(tx,ty)}
                path[newboard] = curpath + [(ty,tx)]
                allcost[newboard] = findCost(newboard, len(curpath)+1)
                seen.add(newboard)
                if newboard == goalboard:found = True;break
    if found:break

if goalboard in path:[print(*i) for i in path[goalboard]]
else:print("Couldn't solve it")