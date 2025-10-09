v14 = [
    0xDAEE93339FD0FB0B,
    0xEA216DC328971117,
    0xA479FCCA28C4D803,
    0x7164D8CB51CBA87B,
    0x762E6B9AC152E344,
    0x9559A26D8B5A914A
]
v15 = 1422678205
v16 = 0
v3 = 11
v4 = 3
v5 = 113
v_bytes = b''.join(v.to_bytes(8, 'little') for v in v14) + v15.to_bytes(4, 'little') + b'\x00'

v6_bytes = v_bytes[1:53]
v6_index = 0

flag = []

while v6_index < len(v6_bytes):
    v8 = pow(v5, v4, 1 << 64)
    v11 = 0
    tmp = v8
    for _ in range(8):
        v11 ^= tmp & 0xFF
        tmp >>= 8

    flag.append(v3 ^ v11)
    v3_new = v6_bytes[v6_index]
    v4_new = v5
    v5_new = v8
    v3, v4, v5 = v3_new, v4_new, v5_new
    v6_index += 1

print(bytes(flag).decode())

# OUTPUT : HZ{coronavirus desease COVID-19 which is virus SAR}