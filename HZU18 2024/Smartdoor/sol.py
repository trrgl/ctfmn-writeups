# 1. decompiler aar ongoilgohod getSecretKey gsn function goor nuuts uge avj bn teriign python der bicy
secret = [0x54, 0x31, 0x72, 0x62, 0x57, 0x38, 0x69, 0x79, 0x6D, 0x7D, 0x69, 0x82, 0x3C, 0x7F, 0x72, 0x6E, 0x7B, 0x44, 0x8B, 0x34, 0x35, 0x36]
flag = ""

for i in range(22):
    v2 = chr(secret[i] - i)
    if v2 == b'\x82':
        flag += chr(119)
    elif v2 == b'\x7f':
        flag += chr(114)
    elif v2 == b'\x8b':
        flag += chr(121)
    else:
        flag += v2

print('HZU18{' + flag + '}')

# OUTPUT : HZU18{T0p_S3cret_w0rd_k3y!!!}