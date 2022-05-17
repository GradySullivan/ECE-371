
import random

#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    ###################################your code goes here#####################################
    # gcd = de + yz

    xy = [0, 0]
    rs1 = [1, 0]
    rs2 = [0, 1]
    negativefixz = z

    while e % z != 0:
        mod = e % z
        quot = e // z
        xy[0] = rs1[0] - quot * rs2[0]
        xy[1] = rs1[1] - quot * rs2[1]

        # swap variables and sets
        rs1 = rs2.copy()
        rs2 = xy.copy()
        e = z
        z = mod

        if xy[0] < 0:
            while xy[0] < 0:
                xy[0] += negativefixz
        d = xy[0]
    return d
    
def is_prime (num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################

    n = p * q
    z = (p-1) * (q-1)  # used to calculate d
    e = random.randint(1, n-1)
    while gcd(e, z) != 1:
        e = random.randint(1, n - 1)
    d = get_d(e, z)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    #cipher=0

    #public key is list with e and n
    # cipher = K+(m) = m^e % n

    encoded = ord(plaintext)
    e = pk[0]
    n = pk[1]

    cipher = pow(encoded, e, n)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext

    d = pk[0]
    n = pk[1]

    plain = pow(ciphertext, d, n)
    plain = chr(plain)
    return ''.join(plain)
