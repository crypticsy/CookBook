'''
#Testing
weight = [3, 2, 6, 8, 2, 6]     #assume characters in a file appears these number of times
tree = {}
for n,i in enumerate(values):
    tree[n] = int(i)
'''



def findmin():
    minkey, minval = -1, float('inf')
    for i in tree.keys():
        if tree[i]<minval:
            minval,minkey = tree[i],i
    tree.pop(minkey)
    return minkey,minval


while len(tree)!=1:         #huffman algo
    smallest1,smalval1 = findmin()
    smallest2,smalval2 = findmin()
    tree[(smallest2,smallest1)] = smalval1+smalval2         # creating a new branch with two smallest and the sum as their value
#print(tree)



allval = {}
def assignkeys(data, cur):
    right, left = "1","0"

    if type(data[0]) is tuple:
        assignkeys(data[0],cur+left)
    else:
        allval[data[0]] = cur+left
    
    if type(data[1]) is tuple:
        assignkeys(data[1],cur+right)
    else:
        allval[data[1]] = cur+right
    


assignkeys(list(tree.keys())[0] , "" )
print(allval)
#print("Max length : ", max(map(len,allval.values())))
