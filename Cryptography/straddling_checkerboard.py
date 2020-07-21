# A straddling checkerboard is a device for converting an alphabetic plaintext into digits. Our checkerboard will look like this :

#   	0  1  2  3  4  5  6  7  8  9
# (0) 	E  T     A  O  N     R  I  S
#  2 	B  C  D  F  G  H  J  K  L  M
#  6 	P  Q  /  U  V  W  X  Y  Z  . 



# Filling the checkerboard

# The first line is filled using a passphrase that contains 2 spaces. We remove letters already used from alphabet to fill the second and the third lines 
# with "/" and "." inserted in.

# Each board cell has a value, whose tens digits is given by the row it's on, and whose units digits is given by the column. First row is always 0; 
# the empty cells in the first row give the values for the second and third lines (2 and 6 here).



# Using the checkerboard

# When encrypting, unsupported characters need to be removed from input message
# The valid characters are letters, digits and the period '.'
# The digits have to be prefixed by the character "/".

# It is now easy to use the grid to encrypt a word :
# - Column value is the units digit
# - Row value is the tenths digit

# By example :
# I am 1 brut => IAM/1BRUT => 8 3 29 62 1 20 7 63 1 => 8329621207631
# The digit is represented by "/" and its value

# Decrypting is easy too :
# 8 => I
# 3 => A
# 2 => empty so we take 20 and add next value = 29 => M
# 6 => 62 => "/" so we take next value => 1
# ...

# Let's make it harder to crack

# To complicate the cracking of the code, let's take a key number : 0432 and use it to modify by addition and modulo 10 the code :

#   8 3 2 9 6 2 1 2 0 7 6 3 1
# + 0 4 3 2 0 4 3 2 0 4 3 2 0
# -------------------------------
#   8 7 5 1 6 6 4 4 0 1 9 5 1


# To construct the number to add , concatenate the key number as many times as necessary. If it is too long, remove the excess numbers at the end (if the code is 059731, the number will be 043204)

# Last step

# The last thing to do is using the checkerboard to convert to characters (letters, slash or period, no digits) :
# 8751664401951 => IRNTXOOETSNT





class StraddlingCheckerboard():

    header, passphrase, pos_Slash_Dot, space1, space2 = [None for x in range(5)]
    checkboard = {}

    def generateCheckboard(self):
        self.checkboard[-1] = list(self.header)
        passphrase = list(self.passphrase)
        self.checkboard[0] = passphrase
        self.space1, self.space2 = [ int(self.checkboard[-1][x]) for x in range(len(passphrase)) if passphrase[x] ==" "]

        letters = [chr(x) for x in range(65,91)]
        for i in passphrase:
            if i != " ":letters.remove(i)

        slash, dot = map(int, self.pos_Slash_Dot.split())
        if dot>slash:
            letters.insert(slash,"/")
            letters.insert(dot,".")
        else:
            letters.insert(dot,".")
            letters.insert(slash,"/")

        self.checkboard[self.space1] = letters[:10]
        self.checkboard[self.space2] = letters[10:]



    def __init__(self,header, passphrase, pos_Slash_Dot):
        self.header = header
        self.passphrase = passphrase
        self.pos_Slash_Dot = pos_Slash_Dot
        self.generateCheckboard()


    def viewCheckerboard(self):
        for i in self.checkboard:print(i,self.checkboard[i])

    

    def encrypt(self, string):
        temp = ""
        for a in list(string):
            if a in self.checkboard[0]:
                pos = self.checkboard[0].index(a)
                temp += self.checkboard[-1][pos]

            elif a in self.checkboard[self.space1]:
                pos = self.checkboard[self.space1].index(a)
                temp +=str(self.space1)+ self.checkboard[-1][pos]

            elif a in self.checkboard[self.space2]:
                pos = self.checkboard[self.space2].index(a)
                temp +=str(self.space2)+ str(self.checkboard[-1][pos])

            elif a in self.checkboard[-1]:
                temp += str(a)

        return temp



    def decrypt(self, string):
        digiter = False
        store = ""
        string = list(string)

        while True:
            if string != []:
                prev = int(string[0])
                head = string.pop(0)
            else:
                break

            if head == str(self.space1) or head == str(self.space2):
                prev2 = int(string[0])
                temp = self.checkboard[int(head)][self.checkboard[-1].index(string.pop(0))]
            else:
                temp = self.checkboard[0][self.checkboard[-1].index(head)]

            if temp == "/":
                if prev2 + int(string[0]) < 10:
                    store+= string.pop(0)
                    digiter = True
                elif int(string[0]) in self.checkboard and self.checkboard[int(string[0])][self.checkboard[-1].index(head)] == ".":
                    store+= string.pop(0)
                    digiter = True
                elif digiter == True:
                    store+= string.pop(0)
                else:
                    store+=temp
            else:
                store+= temp
        
        return store



    def encode(self, action, key, message):
        digit = {" ":"",'0':'/0','1':'/1','2':'/2','3':'/3','4':'/4','5':'/5','6':'/6','7':'/7','8':'/8','9':'/9'}

        for i in digit:
            message = message.replace(i,digit[i])

        message = message.upper()
        encryp =  self.encrypt(message)
        count = 0
        hashed = ""
        if action.lower() == "encrypt":
            for a in range(len(encryp)):
                hashed += str((int(encryp[a])+int(key[count]))%10)
                if count<len(key)-1:
                    count+=1
                else:
                    count = 0
        else:
            for a in range(len(encryp)):
                if int(encryp[a])>=int(key[count]):
                    hashed += str(int(encryp[a])-int(key[count]))
                else:
                    hashed += str(((10+int(encryp[a]))-int(key[count]))%10)
                if count<len(key)-1:
                    count+=1
                else:
                    count = 0
            
        print(self.decrypt(hashed))




'''

# Testing

curheader = "0246897531"    # values for creating checkerboard 
curpassphrase = "AND WE TRY"
curposDotSlash = "17 6"

curaction = "decrypt"
curkey = "666"
curmessage = "TYRWRTNTRYNRYNRYNN/WRWRCITATNQNJYT"


test = StraddlingCheckerboard(curheader, curpassphrase,curposDotSlash)
test.viewCheckerboard()
test.encode(curaction,curkey,curmessage)

'''
