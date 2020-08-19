# The Brainfuck model is composed of three elements:
# - An array of S one byte cells initialized to 0, and indexed from 0.
# - A pointer initialized to point to the first cell (index 0) of the array.
# - A program made up of the 8 valid instructions.

# The following are the instructions:
# - > increment the pointer position.
# - < decrement the pointer position.
# - + increment the value of the cell the pointer is pointing to.
# - - decrement the value of the cell the pointer is pointing to.
# - . output the value of the pointed cell, interpreting it as an ASCII value.
# - , accept a positive one byte integer as input and store it in the pointed cell.
# - [ jump to the instruction after the corresponding ] if the pointed cell's value is 0.
# - ] go back to the instruction after the corresponding [ if the pointed cell's value is different from 0.




data = [0]

# Add the code here
line = "++++++++++[>+++++++>++++++++++>+++<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+." # Output : Hello World!

# Add the inputs here
allinput = []        



def interpreter():
    inputcounter,pointer = 0,0
    if line.count("[")!=line.count("]"):print("SYNTAX ERROR");return
    output,i = "",0
    while i <len(line):
        if line[i] == ">":
            pointer +=1
            if pointer>len(data)-1:data.append(0)
        
        elif line[i] == "<":
            pointer -=1
            if pointer==-1:print("POINTER OUT OF BOUNDS");return

        elif line[i] == "+":
            data[pointer] +=1
            if data[pointer]>255:print("INCORRECT VALUE");return 

        elif line[i] == "-":
            data[pointer] -=1 
            if data[pointer]<0:print("INCORRECT VALUE");return

        elif line[i] == ".":output += chr(data[pointer])

        elif line[i] == "[":
            if data[pointer]==0:
                acount, bcount,pos = 1, 0, i
                while acount != bcount:
                    pos+=1
                    if line[pos] == "[":acount+=1
                    elif line[pos] == "]":bcount+=1
                i=pos
            
        elif line[i] == "]":
            if data[pointer]!=0:
                acount, bcount,pos = 0, 1, i
                while acount != bcount:
                    pos-=1
                    if line[pos] == "[":acount+=1
                    elif line[pos] == "]":bcount+=1
                i=pos
        

        elif line[i] == ",":
            data[pointer] = allinput[inputcounter]
            inputcounter+=1

        i+=1

    print(output)


interpreter()