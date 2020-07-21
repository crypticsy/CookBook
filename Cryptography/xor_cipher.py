# At RobberCity, it's really hard to send a parcel safely. Postmen are thiefs, and you can be sure that without a proper lock, your box will be opened 
# and emptied prior to "delivery".
# This is a famous riddle: how can Alice send a parcel to Bob, without having to send the lock key?

# Alice and Bob decided to use the riddle solution applied to XOR.
# * step 1: Alice encodes her message with her random key, as long as the message itself. She sends it to Bob
# * step 2: Bob encodes the ciphered message with his own random key, as long as the message itself. He sends it back to Alice
# * step 3: Alice decodes the message with her initial key, and sends it to Bob
# * step 4: Bob decodes the message with his initial key, and gets the clear text.

# And it works! XOR is both commutative and associative, and A XOR 0 = A and A XOR A = 0. Hence
# Message XOR AliceKey XOR BobKey XOR AliceKey XOR BobKey
#  = Message XOR (AliceKey XOR AliceKey) XOR (BobKey XOR BobKey)
#  = Message XOR 0 XOR 0
#  = Message

# You're a man-in-the-middle, intercepting any message between Alice and Bob.
# (Btw, your existence proves that they both really had good reasons to put a data cipher process in place...)
# So, you intercept the 3 messages message1, message2 and message3.

# Your goal is to be smarter than the smarties, and to break their code.




def xor(a, b):
    x = "{0:08b}".format(int(a, 16))
    y = "{0:08b}".format(int(b, 16))
    value = ""
    for c in range(len(x)):
        value += str( int(x[c]) ^ int(y[c]) )

    return '%02X' % int(value, 2)

m1 = "391813c092a2d5ac9acb705dfe41be3df08de67d1145cbcc3f"
m2 = "03adeae2c8c2f2336c8a8d312733c2456e76e0b2d9068adc3f"
m3 = "72d0954e354045f09461dc4c911d0b58ff8963efb12c34303f"


output = ""
for i in range(0,len(m1),2):
    key = xor(m1[i:i+2],m2[i:i+2])
    temp = xor(key,m3[i:i+2])
    output += chr(int(temp,16))
    
print(output)           # Output : Hello bob ! How are you ?
