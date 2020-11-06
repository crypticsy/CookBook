single = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
exclude = {'11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
double = {'1':'ten','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
zero = {3:'thousand',6:'million',9:'billion',12:'trillion',15:'quadrillion',18:'quintillion'}


def translate(n):
    if int(n)==0: return ['zero']

    output = []
    if n[0] == "-": output.append('negative');n=n[1:]
    x = len(n) if len(n)%3 ==0 else len(n)+3-len(n)%3 
    n = n.rjust(x, "0")

    while n!="":
        if n[0] in single: output += [ single[n[0]], 'hundred']
        if n[1:3] in exclude:
            output.append(exclude[n[1:3]])
        else:
            temp = []
            if n[1] in double: temp.append(double[n[1]])
            if n[2] in single: temp.append(single[n[2]])
            if temp!=[]: output.append('-'.join(temp))
        n = n[3:]        
        if len(n) in zero: output.append(zero[len(n)])
        if n!="" and int(n) == 0:break

    return output


n = int(input("Enter the range of inputs: "))
for i in range(n):
    print(*translate(input("Enter the number you wish to translate: ")))