from Crypto.Util.number import *
from math import gcd
import ast

with open("output.txt") as f:
    lines = f.read().splitlines()

R = ast.literal_eval(lines[0].split(" = ")[1])
n = int(lines[1].split(" = ")[1])
c = int(lines[2].split(" = ")[1])

def parinad(n):
    return bin(n)[2:].count('1') % 2

def vinad(x, R):
    return int(''.join(str(parinad(x ^ r)) for r in R), 2)

for r in range(1 << 20):
    p = vinad(r, R)
    if not isPrime(p):
        continue
    if n % p != 0:
        continue
    q = n // p
    e = vinad(r + 0x10001, R)
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        continue

    d = inverse(e, phi)
    m_sum = pow(c, d, n)
    m = m_sum - sum(R)

    try:
        flag = long_to_bytes(m)
        if b"CCTF{" in flag:
            print(flag.decode())
            break
    except:
        continue
else:
    print("baidgue pzda")
