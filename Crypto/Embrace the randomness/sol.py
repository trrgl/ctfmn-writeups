with open("output.txt", "r") as f:
    lines = f.read().splitlines()

flag = ""

all_bytes = set(range(256))

for i in range(42):
    data = []
    for line in lines:
        data.append(line[(2*i):(2*i+2)])
    present = set(int(a, 16) for a in data)
    missing_byte = all_bytes - present
    flag += chr(missing_byte.pop() ^ 255)

print(flag)

# HZU18{B3_CAREFUL_0N_CUSTOM_1MPL3M3NTATION}