# key n 8 iin urttai, flag format n 7iin urttai bolhoor suulin byte iig bruteforce lhdl bolno
def xor(x, y):
    result = []
    length = max(len(x), len(y))
    for i in range(length):
        result.append(x[i % len(x)] ^ y[i % len(y)])
    return bytes(result)

enc = bytes.fromhex('4728d7c027e2e172467dcafe2db3e8794b1df29038dcf3795a26ffd57fedee69')
known = b'mazala{'
key = []
for i in range(7):
    key.append(enc[i] ^ known[i])

for i in range(256):
    temp_key = []
    for a in key:
        temp_key.append(a)
    temp_key.append(i)
    flag = xor(temp_key, enc)
    if chr(flag[-1]) == '}':
        print(flag.decode())

# OUTPUT : mazala{fl4g_f0rmaT_1s_impoRt4nt}