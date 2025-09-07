import itertools
import random

with open('flag.enc', 'rb') as f:
    data = f.read()

enc_flag = data[:-18]
enc_now = data[-18:]

now = bytearray()
for _ in enc_now:
    now.append(_ ^ 0x42)

now = now.decode()
random.seed(now)
message = ""

for _ in enc_flag:
    message += chr(_ ^ random.randrange(256))

print(message)
perms = list(itertools.permutations(range(8)))

def decrypt_stage_one(message, key):
    lengths = [4, 4, 4, 3, 3, 3, 3, 3]
    parts = []
    count = 0
    res = ''
    for _ in key:
        start = count
        end = count+lengths[_]
        parts.append((message[start:end], _))
        count += lengths[_]
    sorted_parts = sorted(parts, key=lambda x: x[1])
    index = 0
    count = 0
    for _ in range(len(message)):
        res += sorted_parts[count][0][index]
        if count >= 7:
            count = 0
            index += 1
        else:
            count += 1
    return res

for perm in perms:
    flag = message
    for _ in range(42):
        flag = decrypt_stage_one(flag, perm)
    if 'ccsCTF' in flag:
        print('[+] FLAG OLCHOO :', flag)
        break
    else:
        print('[+] Perm :', perm)
        print('[+] Failed :', flag)

# OUTPUT : ccsCTF{w0w_y0u_G07_17!!!!!}