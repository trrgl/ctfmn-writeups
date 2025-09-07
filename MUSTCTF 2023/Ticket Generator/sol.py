from Crypto.Util.number import *
e = 65537
n = 882564595536224140639625987659416029426239230804614613279163
c = 0x5dc3e1d09a42233cc160a1c5bba4100f2556b5ef933d20c5ca
p = 857504083339712752489993810777 # factordb.com
q = 1029224947942998075080348647219 # factordb.com
if p * q != n:
    print("TAARAHGU BNSHDE PSDDA")
phi = (p-1) * (q-1)
d = inverse(e, phi)
flag = b'MUSTCTF{' + long_to_bytes(pow(c,d,n)) + b'}'
print(flag.decode())

# OUTPUT : MUSTCTF{da59ec40ce31b9c46ef2a8ff5}