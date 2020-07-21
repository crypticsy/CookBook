# Problem : You are given 2 expressions representing 2 numbers written in roman numerals.
#           You have to provide the result of the sum of these 2 numbers, also in roman numerals.

class RomanNumeralSystem():
    check,decheck = None, None

    def __init__(self):
        vhigh = {'MMMM':4000,'MMM':3000,'MM':2000,}
        decvhigh = { vhigh[x]:x for x in vhigh.keys()}
        decvhigh[1000] = 'M'

        high = {'CD':400,'CM':900,'M':1000,'DCCC':800,'DCC':700,'DC':600,'D':500,'CCC':300,'CC':200}
        dechigh = { high[x]:x for x in high.keys()}
        del dechigh[1000]
        dechigh[100] = 'C'

        mid = {'XL':40,'XC':90,'C':100,'LXXX':80,'LXX':70,'LX':60,'L':50,'XXX':30,'XX':20}
        decmid = { mid[x]:x for x in mid.keys()}
        del decmid[100]
        decmid[10] = 'X'

        low = {'IV':4,'IX':9,'X':10,'VIII':8,'VII':7,'VI':6,'V':5,'III':3,'II':2,'I':1}
        declow = { low[x]:x for x in low.keys()}
        del declow[10]

        self.check = [vhigh,high,mid, low]
        self.deccheck = [declow,decmid,dechigh,decvhigh]



    def romToDec(self,x):
        val = 0
        
        sep = []
        y = x
        while y!='':
            for a in self.check:
                breaker = False
                for i in a.keys():
                    if i in y:
                        y = y.replace(i,'')
                        sep.append(i)
                        breaker = True
                        break
                if breaker: break
        
        
        for a in sep:
            for i in self.check:
                if a in i:
                    val += i[a]
                    break
        
        return val

    def addRomans(self, rom_1, rom_2):
        total = self.romToDec(rom_1) + self.romToDec(rom_2)

        output = ""
        rem=10
        for i in self.deccheck:
            n = total % rem
            if n in i:output = i[n]+output
            total = total - n
            rem = rem *10

        print(output)


# Testing

test = RomanNumeralSystem()
test.addRomans("VI","VII")
test.addRomans("XII","XXVII")
test.addRomans("CXXIII","CCCXXI")
test.addRomans("MMXVI","CMXCIX")
