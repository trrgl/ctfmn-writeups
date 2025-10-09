from itertools import product
from math import gcd

p = 79565304973649738046890929641550086406229645142982116252431882783628570446741
q = 104895446414749804110599905404014579424417002368568255490767700901764221803853
c = 4540356813631057206329938934275504497042552943607683102015080934372428231345551929844529058302190596843384780497234278626232722159254772622184794355722055
e = 2**16

# Extended Euclidean algorithm for modular inverse
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % m

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

# Tonelli–Shanks for modular sqrt
def mod_sqrt(a, p):
    if a % p == 0:
        return [0]
    if pow(a, (p - 1) // 2, p) != 1:
        return []  # No square root exists
    if p % 4 == 3:
        r = pow(a, (p + 1) // 4, p)
        return [r, p - r]
    q_, s = p - 1, 0
    while q_ % 2 == 0:
        q_ //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q_, p), pow(a, q_, p), pow(a, (q_ + 1) // 2, p)
    while t != 1:
        i, t2 = 1, pow(t, 2, p)
        while t2 != 1:
            t2 = pow(t2, 2, p)
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, pow(b, 2, p), (t * pow(b, 2, p)) % p, (r * b) % p
    return [r, p - r]

# Repeatedly take square roots k times
def repeated_sqrt(c, prime, k):
    values = [c % prime]
    for _ in range(k):
        new_vals = []
        for v in values:
            roots = mod_sqrt(v, prime)
            new_vals.extend(roots)
        if not new_vals:
            return []
        values = list(set(new_vals))
    return values

k = 16
roots_p = repeated_sqrt(c, p, k)
roots_q = repeated_sqrt(c, q, k)

print(f"Roots mod p: {len(roots_p)}, Roots mod q: {len(roots_q)}")

# Combine with CRT
def crt(a1, m1, a2, m2):
    inv_m1 = modinv(m1, m2)
    return (a1 + (a2 - a1) * inv_m1 % m2 * m1) % (m1 * m2)

if roots_p and roots_q:
    candidates = []
    for rp, rq in product(roots_p, roots_q):
        m = crt(rp, p, rq, q)
        candidates.append(m)
    # Convert to bytes and filter by known format
    for m in candidates:
        b = m.to_bytes((m.bit_length() + 7) // 8, 'big')
        if b.startswith(b"mazala{") and b.endswith(b"}"):
            print("Possible flag:", b.decode())
else:
    print("No roots found for given p and q.")

# Flag : mazala{m0dul4r_Square_r00t}