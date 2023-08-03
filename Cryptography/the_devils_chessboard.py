### The Devil's Chessboard Problem

# The devil has captured two people and is playing a game with them for their freedom. 
# Person A will be presented with a chessboard with a penny in each square (64 total), with each penny either heads up or tails up randomly. 
# The devil will choose a particular square and point it out to Person A. 
# Person A then chooses a single square, and flips the penny in that square. 
# Afterward, Person A is sent away and Person B is brought forward. 
# Based on the new state of the board, Person B must point out the same square that the devil did in order to win. 
# The two people can devise a strategy beforehand, but cannot communicate once the game starts. How can they win?


# --- Solution

# 1. Look at the positions of the coins showing heads.
#       Example assume : 2, 11, 17, 22, 46, and 62 have heads in them
#       The devil pointed at 53

# 2. Write the cell number of each of these coins as a six-digit binary code from 000000 to 111111.
#    Place these numbers in a vertical list.
#         2   =   0 0 0 0 1 0
#         11  =   0 0 1 0 1 1
#         17  =   0 1 0 0 0 1
#         22  =   0 1 0 1 1 0
#         46  =   1 0 1 1 1 0
#         62  =   1 1 1 1 1 0

# 3. For each column write 0 if the count 1s in that column is even, write 1 otherwise. This gives an
#    “auxiliary” six-digit code.
#         2   =   0 0 0 0 1 0
#         11  =   0 0 1 0 1 1
#         17  =   0 1 0 0 0 1
#         22  =   0 1 0 1 1 0
#         46  =   1 0 1 1 1 0
#         62  =   1 1 1 1 1 0
#       -----------------------
#                 1 0 1 0 1 1

# 4. Compare the auxiliary code with the six-digit code of the cell number of the favored coin. 
#    For each position along that code, write 1 if there is a mismatch of digits, write 0 otherwise. 
#    This gives yet another six-digit code. This is the code of the cell number of the coin you flip. 
#    You’ve now arranged matters so that the heads on the board encode the cell number of the favored coin.
#                 1 0 1 0 1 1   (auxiliary code)
#                 | | | | | |
#                 v v v v v v
#                 1 1 0 1 0 1   (53, the square pointed by devil)
#               ---------------
#                 1 1 0 1 0 1   (favored coin position)




import numpy as np

class Chessboard:

    def __init__(self):
        """ Creates an instance of the Chessboard class """

        # Devil sets the chessboard in an arbitrary configuration,
        # in an effort to frustrate your system.
        # True if Tails, False if Heads
        self.x = np.random.choice(a=[True, False], size=(8, 8), p=[0.5, 0.5])

        # We label the squares of the chessboard from 0 to 63
        self.labels = np.reshape(np.arange(64), (8,8))


    # --- Helper functions ---

    def getParity(self, val:list):
        # parity refers to whether a number is odd or even
        # even numbers have parity 0 because x%2 = 0, if x is even
        # odd numbers have parity 1 because x%2 = 1, if x is odd
        # a collection of 0s and 1s can also have a parity -- which would tell you whether its sum is even or odd

        # returns 1 if sum of values is odd else 0
        return int(sum(val) % 2 == 0)
    
    def to_decimal(self, val:list):
        return int("".join(map(str, val)), 2)

    def read_board(self):
        # find all the heads
        heads = self.labels[~self.x]
        
        # convert all labels to a six digit binary code
        binary = np.array([np.array(list('{0:06b}'.format(num))) for num in heads ])
        
        return [ self.getParity(binary[:, x].astype(int)) for x in range(6)]
    
    

    def encode(self, pos: int):
        """Flip the coin based on the position of ticket"""
        key = list('{0:06b}'.format(pos))
        
        auxiliary_code = self.read_board()
        
        flip_binary_pos = [int(key[n]) ^ int(auxiliary_code[n]) for n in range(6)]
        flip_pos = np.where( self.labels == self.to_decimal(flip_binary_pos))
        
        # flip the value of the desired location for encryption
        self.x[flip_pos] = ~self.x[flip_pos]

        print("--- Encoded board ---")
        print(self.x)
    

    def decode(self):
        """ Defines how to read the chessboard """
        auxiliary_code = self.read_board()
        
        print("--- Decoded message ---")
        print(self.to_decimal(auxiliary_code))



problem = Chessboard()
problem.encode(47)
print("\n")
problem.decode()