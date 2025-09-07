# factordb.com oos public key gee p, q huvaj 
from Crypto.Util.number import inverse, long_to_bytes

c = 38625589080883093104580367978310695507327838321390248676015440812648307006611
e = 0x10001
p = 176773485669509339371361332756951225661
q = 333197218785800427026869958933009188427
phi = (p-1) * (q-1)
n = p*q

d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))

# OUTPUT : HZU18{RS4_is_v3ry_EZ}