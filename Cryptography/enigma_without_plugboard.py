class EnigmaWithoutPlugboard():

    rotor1, rotor2 , rotor3, trig1, trig2, trig3, reflector = [None for x in range(7)]

    def __init__(self, rot1, rot2, rot3, t1, t2, t3, reflec):
        
        self.rotor1 = {x[0]:x[2] for x in rot1.split()}
        self.trig1 = t1

        self.rotor2 = {x[0]:x[2] for x in rot2.split()}
        self.trig2 = t2

        self.rotor3 = {x[0]:x[2] for x in rot3.split()}
        self.trig3 = t3
        
        self.reflector = {x[0]:x[2] for x in reflec.split()}



    def encode(self, pos, message):
        r1, r2, r3 = pos.split()
        alphabet = [chr(65+x) for x in range(26)]
        back = {alphabet[x]:alphabet[x-1] for x in range(26)}

        rotor1 = self.rotor1
        for i in range(ord(r1)-65):
            newr1 = {} #values for the ever changing rotor 1
            for a in rotor1.keys():newr1[back[a]] =back[rotor1[a]]
            rotor1 = newr1

        rotor2 = self.rotor2
        for i in range(ord(r2)-65):
            newr2 = {} #values for the ever changing rotor 2
            for a in rotor2.keys():newr2[back[a]] =back[rotor2[a]]
            rotor2 = newr2

        rotor3 = self.rotor3
        for i in range(ord(r3)-65):
            newr3 = {} #values for the ever changing rotor 2
            for a in rotor3.keys():newr3[back[a]] =back[rotor3[a]]
            rotor3 = newr3

        revrotor2 = {a:b for b,a in rotor2.items()}
        revrotor3 = {a:b for b,a in rotor3.items()}


        output = ""
        rot2val = False
        for i in message:
            if r2 == trig2 and rot2val:
                rot2val = False
                r3 = chr(65+(ord(r3)+1-65)%26)
                newr3 = {} #values for the ever changing rotor 3
                for a in rotor3.keys():newr3[back[a]] =back[rotor3[a]]
                rotor3 = newr3
                revrotor3 = {a:b for b,a in rotor3.items()}
                r2 = chr(65+(ord(r2)+1-65)%26)
                newr2 = {} #values for the ever changing rotor 2
                for a in rotor2.keys():newr2[back[a]] =back[rotor2[a]]
                rotor2 = newr2
                revrotor2 = {a:b for b,a in rotor2.items()}
                rot2val = True


            if r1 == trig1:
                r2 = chr(65+(ord(r2)+1-65)%26)
                newr2 = {} #values for the ever changing rotor 2
                for a in rotor2.keys():newr2[back[a]] =back[rotor2[a]]
                rotor2 = newr2
                revrotor2 = {a:b for b,a in rotor2.items()}
                rot2val = True
            
            

            newr1 = {} #values for the ever changing rotor 1
            for a in rotor1.keys():newr1[back[a]] =back[rotor1[a]]
            rotor1 = newr1
            revrotor1 = {a:b for b,a in rotor1.items()}
            r1 = chr(65+(ord(r1)+1-65)%26)

            

            #the entire process
            curr = rotor1[i]
            curr = rotor2[curr]
            curr = rotor3[curr]
            curr = self.reflector[curr]
            curr = revrotor3[curr]
            curr = revrotor2[curr]
            curr = revrotor1[curr]

            output += curr


        print(output)


# Testing 

# Values for creating the enigma
Rot1 = "A-A B-J C-D D-K E-S F-I G-R H-U I-X J-B K-L L-H M-W N-T O-M P-C Q-Q R-G S-Z T-N U-P V-Y W-F X-V Y-O Z-E"
Rot2 = "A-E B-K C-M D-F E-L F-G G-D H-Q I-V J-Z K-N L-T M-O N-W O-Y P-H Q-X R-U S-S T-P U-A V-I W-B X-R Y-C Z-J"
Rot3 = "A-V B-Z C-B D-R E-G F-I G-T H-Y I-U J-P K-S L-D M-N N-H O-L P-X Q-A R-W S-M T-J U-Q V-O W-F X-E Y-C Z-K"
trig1 = "E"
trig2 = "Q"
trig3 = "Z"
reflector = "A-Y B-R C-U D-H E-Q F-S G-L H-D I-P J-X K-N L-G M-O N-K O-M P-I Q-E R-B S-F T-Z U-C V-W W-V X-J Y-A Z-T"


test = EnigmaWithoutPlugboard(Rot1, Rot2, Rot3, trig1, trig2, trig3, reflector)
message = "EODHXKGLWRIVTFXPXBRPLOOWSUIQQWJAXZTSKHQTNBVDAQFGIXLPHUCRLLYFWYUGQULEOQQQUGJMMZQIKPRTGQGWCMGRBPRDXZACQBHYQWNNRRCPKRZIOZRBCVRCHXQUFYOUICWHPYKWCNVDYWEGOLSWXGGAIMIJXEADPACBTKLLNUVIIERERQEXOBSLHXZKQUYBNMYVVHRQAHZQUUXAUOWJTHQHHNTKRQYKMHLAYUZPRYTIWHTDFACQLAWAWGCMHBLTAQPJNLQQXDISNTVQYXKUHVTHXNZQMROSUBUKWHJGIOGEFWXMJOWSXFJZBIPCHWZXYFUDVZPXCDFVTQZSXEIETRGRILUKPKKJFFISNPZCFIQOXFZGTOUUUPVACLAORNQDHAKDAXDQEWEZQSCCPUPIHOHWELLSQUIVUYYCBIPRHZAKBBUMXPQXNNXPITDJLPOYLSCOFJMYYHESZYWPPKMEVBVLMALDUGDUSTZMZWAHKAJOKYDKKIJJELKWFZWVWNRQVYUTFWALUGNNUXHUVLJHVFPRRKGGASBTHNEJPMINNGYVUXHGNWELGCSTUMCBQEWQJOAVRCPGEOQFTOMWWMCRTLMLRGXITRLYXBZEANENGAHFECEMDSXBZLVBHGNAQLJTMZKTIKZLVNDBZNPNBIQFDHNYBRTVGUVQFOYPQUVWSEMXNIPXOJHZTCQSEWSGZAKUQSCCKVVVOKEPRGJUYJYYRXMGLYHQJVAOVNDVWVTCEZLWQFMLFNYSCRCNFXNCFCMBENTMXNNQWNFNSXSMCWWLLPTMYNWFJMEGYYWFZKKYDTBIXAMXBXXUUVIYPMTRBYSNHBBQGOJKZSVATOPPOVVJCRNPHJWJKHPISHPSLMNAXYPONKTPBQGGFVFCKQOJKCBKHFLMAXXJYTNRFEFALUBMGTWWEAEFRQEZJMJIAJOYMQYMPHQQFKMKKQBEWDGMBUJVQBCAOISHNJXNSJZOWQXQRDYM"
test.encode("G P L",message)
