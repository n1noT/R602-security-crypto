from random import *
import Cryptodome.Random.random
import Cryptodome.Util.number
import math

def prime_gen(l):
    p = Cryptodome.Random.random.getrandbits(l)
    while not Cryptodome.Util.number.isPrime(p):
        p = Cryptodome.Random.random.getrandbits(l)
    return p

def gen_unit(m):
    e = randint(2, m)
    while math.gcd(e, m) != 1:
        e = randint(2, m)
    return e

def KGen(l):
    p = prime_gen(l//2)
    q = p 
    while q == p:
            q= prime_gen(l//2)
    e = gen_unit((p-1)*(q-1))
    d = Cryptodome.Util.number.inverse(e, (p-1)*(q-1))
    pk = [e, p*q]
    sk = [d, p, q]

def Enc(pk, m):
    e = pk[0]
    n = pk[1]
    return pow(m, e, n)

def Dec(sk, c):
    d = sk[0]
    n = sk[1] * sk[2]
    return pow(c, d, n)
