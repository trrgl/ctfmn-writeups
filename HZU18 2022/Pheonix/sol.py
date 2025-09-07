from hashlib import sha256

N = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
r = 102369864249653057322725350723741461599905180004905897298779971437827381725266
s1 = 86017297084121531012120513768216972928403225965629451161940398986923165378429
s2 = 117330022099634898538735287869957120561139211618198729888688532205377661160

m1 = b"hello world"
m2 = b"hi world"

e1 = int.from_bytes(sha256(m1).digest(), "big")
e2 = int.from_bytes(sha256(m2).digest(), "big")

def modinv(a, n):
    return pow(a, -1, n)

k = ((e1 - e2) * modinv(s1 - s2, N)) % N

d = ((s1 * k - e1) * modinv(r, N)) % N

print("Recovered privKeyD =", hex(d))

# FLAG : HZU18{6181d3016a21dbf346f14b52abac9984b18289d80d09ba94ad32a36eb6da3d6e}
