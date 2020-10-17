import sys
import math
def bfs(map,sx,sy,dx,dy):
    visited=[[False for i in range(10)]for k in range(10)]
    a=[]
    r=0
    a.append((sx,sy,0))
    run=True
    while len(a)>0 and run:
        th=a[0]
        a=a[1:]
        x=th[0]
        y=th[1]
        d=th[2]
        tx=x
        ty=y
        if tx==dx and ty==dy:
            run=False
            r=d
        else:
            if map[min(9,x+1)][y]==0 and not visited[min(9,x+1)][y]:
                a.append((x+1,y,d+1))
                visited[min(10,x+1)][y]=True
            if map[max(0,x-1)][y]==0 and not visited[max(0,x-1)][y]:
                a.append((x-1,y,d+1))
                visited[max(0,x-1)][y]=True
            
            if map[x][min(9,y+1)]==0 and not visited[x][min(9,y+1)]:
                a.append((x,y+1,d+1))
                visited[x][min(10,y+1)]=True
            
            if map[x][max(0,y-1)]==0 and not visited[x][max(0,y-1)]:
                a.append((x,y-1,d+1))
                visited[x][max(0,y-1)]=True            
    return r
map=[[0 for i in range(10)]for j in range(10)]
for i in range(10):
    row = input()
    for j in range(10):
        if row[j]=="#":
            map[j][i]=1
        if row[j]=="C":
            sx=j
            sy=i
        if row[j]=="M":
            dx=j
            dy=i
print(str(bfs(map,sx,sy,dx,dy)*10)+"km")
