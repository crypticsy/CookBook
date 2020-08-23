# Elliptic-Curve Cryptography (ECC) is a recent approach to asymmetric cryptography. Its main benefit is an excellent ratio between the level of security and the key size. 
# For example, the NSA recommends 384-bit keys for a top-secret level encryption using ECC, while achieving the same level of security using RSA requires 7680-bit keys. 
# RSA is currently mostly used with 1024-bit keys, which is equivalent to 160-bit keys with ECC (Ref #1).

# How it works

# Given a prime number P, an elliptic curve (over a finite field) is the set of points (X,Y), 0 ≤ X,Y < P, verifying an equation of the 
# form Y² = X^3 + A*X + B mod P for some fixed parameters 0 ≤ A,B < P. 

# In this puzzle, we use one of the most common curve (used for bitcoin): secp256k1 having the equation Y² = X^3 + 7, usually modulo a 256-bit prime number
#  which we replace here by a 62-bit prime (for an easier manipulation in any programming language).

# Let us define an addition operator on the curve points (see Ref #3 for a visual illustration).
# To double a point C: Consider the tangent to the curve at point C. Let (X,Y) be its intersection with the curve, the point S = 2C is defined as (X,-Y).
# To add two distinct points C and D: Consider the line passing through both points. Let (X,Y) be its intersection with the curve, the point S = C+D is defined as (X,-Y).

# Let us consider a starting point G on the curve and generate a public key as k*G (i.e. G+G+...+G k times) for some randomly chosen integer k which will be the private key. 
# This pair of public/private keys can be used to encrypt or sign messages (e.g. through ElGamal cryptosystem), yet this is out of the scope of this puzzle. 
# The safety of the private key is not based on the public value G but on the difficulty of retrieving k given k*G (known as the Discrete Log problem). 
# k is often above 2^200 to make sure not to be able to bruteforce it. As a result, to compute your key in an efficient way, you should use the double-and-add method (Ref #4).

# Explicit formulas

# To compute S = (Xs,Ys) = C+D given two distinct points C = (Xc,Yc) and D = (Xd,Yd):
# L  = (Yd - Yc) / (Xd - Xc)  mod P
# Xs = L² - Xc - Xd           mod P
# Ys = L * (Xc - Xs) - Yc     mod P
# To double a point, i.e. when C = D, L becomes (here A = 0):
# L  = (3*Xc^2 + A) / (2*Yc)  mod P
# Note: You will have to compute a modular division, a division modulo P.







import sys
import math
  

def karatsuba(num1,num2):
	if num1 < 10 or num2 < 10: return num1 * num2		#base case
	halfmax = max(len(str(num1)),len(str(num2))) // 2 
	a = num1 // 10**(halfmax)
	b = num1 % 10**(halfmax)	
	c = num2 // 10**(halfmax)
	d = num2 % 10**(halfmax)
	ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	ad_plus_bc = karatsuba((a+b),(c+d)) - ac - bd
	return ac * 10**(2*halfmax) + (ad_plus_bc * 10**halfmax) + bd


def modDivide(a,b,m): 
    a = a % m 
    g = math.gcd(b, m)
    if g!=1: return None
    else: return karatsuba(pow(b, m - 2, m), a) % m




A = 0
B = 7
P = int(0x3fddbf07bb3bc551)
G = (int(0x69d463ce83b758e), int(0x287a120903f7ef5c))     #starting point


k = "0x6f"          # some hex value

point = None
for _ in range(int(k,0)-1):
    seen = set()
    if _ == 0:
        slope = modDivide( (3*G[0]**2 + A) , (2*G[1]), P)
        x = (karatsuba(slope, slope) - G[0]*2)% P
        y = (karatsuba(slope,(G[0] - x)) - G[1])% P
        point =  (x,y)

    else:
        slope = modDivide( (point[1] - G[1]) , (point[0] - G[0]), P)
        x = (karatsuba(slope, slope) - G[0] - point[0]) % P
        y = (karatsuba(slope,(G[0] - x)) - G[1])% P
        point =  (x,y)


print(hex(point[0]))        # public key
