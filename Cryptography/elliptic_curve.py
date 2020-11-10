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

def mod_inv(x, P):return pow(x, P-2, P)

def point_add(C, D, P):
    if C == (0, 0): return D
    L = ((D[1] - C[1]) * mod_inv(D[0] - C[0], P)) % P
    X = (L*L - C[0] - D[0]) % P
    Y = (L * (C[0] - X) - C[1]) % P
    return (X, Y)

def point_double(C, P):
    L = ((3 * (C[0]*C[0])) * mod_inv(2*C[1], P)) % P
    X = (L*L - C[0] - C[0]) % P
    Y = (L * (C[0] - X) - C[1]) % P
    return (X, Y)


def elliptic_curve(start, n, P):
    N = start
    Q = (0, 0)
    i = 1
    while i <= n:
        if n & i == i:
            Q = point_add(Q, N, P)
        N = point_double(N, P)
        i *= 2
        
    return hex(int(Q[0]))        # public key



A = 0
B = 7
P = 0x3fddbf07bb3bc551
G = (0x69d463ce83b758e, 0x287a120903f7ef5c)         # starting point

# k = int(input(),0)
k = "0x6f"          # some hex value

print( elliptic_curve( G, k, P) )
