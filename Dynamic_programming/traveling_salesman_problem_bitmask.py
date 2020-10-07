# The travelling salesman problem asks the following question: 

# "Given a list of cities and the distances between each pair of cities, 
# what is the shortest possible route that visits each city and returns to the origin city?"



import os, sys
sys.setrecursionlimit(10**6) 


path = os.path.dirname(os.path.abspath(__file__))
values = list(open( path +'\\tspdemo.txt','r'))     # Use a file that contains the co-ordinates separated by space where each new co-od is in a new line


def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 )**0.5

cost = {}
for i in range(len(values)):
    curCo = list(map(float, values[i].split()))
    for j in range(i+1, len(values)):
        temp =  distance(curCo, list(map(float, values[j].split())) )
        cost[(i,j)] = cost[(j,i)] = temp


num = len(values)
allVisisted = (1<<num)-1

memo = {}
def tsp(mask, pos):
    if mask == allVisisted:return cost[(pos, 0)]
    if (mask,pos) in memo:return memo[(mask,pos)]

    mini = float('inf')
    for city in range(num):
        if mask & (1<<city) == 0:
            mini = min(mini, cost[(pos, city)] + tsp(mask|(1<<city),city))
    
    memo[(mask,pos)] = mini
    return mini

print(tsp(1, 0))