r5 = [101, 123, 138, 19, 31, 73, 8, 13, 1, 79, 11, 58, 92, 10, 44, 14, 32, 115, 40, 74, 41, 3, 204, 14, 1, 21, 62, 18, 18, 39, 113, 123, 108, 117, 183, 119, 182, 33, 96]

def complexTransform(c, idx, k=43):
    r1 = c ^ k
    r1 = r1 + ((idx*idx) % 7)
    if idx % 2 == 0:
        r1 = r1 - idx
    else:
        r1 = r1 + idx
    r1 = r1 ^ ((idx + 3) << 1)
    return r1 & 0xff

flag_chars = []
for i, target in enumerate(r5):
    found = None
    for c in range(32, 127):
        if complexTransform(c, i, 43) == target:
            found = chr(c)
            break
    flag_chars.append(found if found else "?")

flag = "".join(flag_chars)
print("Recovered flag:", flag)

# Flag : HZU18{495a22a7719c9d1584f919cbf5c3530c}