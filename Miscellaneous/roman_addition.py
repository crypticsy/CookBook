# Problem : You are given 2 expressions representing 2 numbers written in roman numerals.
#           You have to provide the result of the sum of these 2 numbers, also in roman numerals.

class RomanNumeralSystem:
    roman, decimal = None, None

    def __init__(self):
        self.roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'':0}
        self.decimal = {self.roman[x]:x for x in self.roman}

    def romToDec(self,mes):
        total, tempo, cur = 0,0,""
        for i in mes:
            if i != cur:total,cur,tempo = total + tempo if self.roman[cur]>self.roman[i] else total - tempo, i,self.roman[i]
            else:tempo+= self.roman[cur]
        total += tempo

        return total


    def decToRom(self,mes):
        output, rem = "",1
        for n in str(mes)[::-1]:
            temp = ""
            if n == "1" or n == "2" or n == "3": temp = self.decimal[1*rem] * int(n)
            elif n == "4":temp = self.decimal[1*rem] * int(n) if rem == 1000 else self.decimal[1*rem]+self.decimal[5*rem]
            elif n == "5" or n == "6" or n =="7"or n =="8":temp = self.decimal[5*rem] + self.decimal[1*rem]  * (int(n)-5)
            elif n == "9":temp =  self.decimal[1*rem]+self.decimal[10*rem]
            rem*=10
            output = temp + output
        return output


    def addRomans(self, rom_1, rom_2):
        total = self.romToDec(rom_1) + self.romToDec(rom_2)
        print(self.decToRom(total))


# Testing

test = RomanNumeralSystem()
test.addRomans("VI","VII")      
test.addRomans("XII","XXVII")
test.addRomans("CXXIII","CCCXXI")
test.addRomans("MMXVI","CMXCIX")
