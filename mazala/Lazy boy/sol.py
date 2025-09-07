# 1. strings dher compiledsn python buyu .pyc gdgn todorhoi bolno
bytes = [122, 94, 50, 82, 75, 92, 125, 67, 92, 94, 101, 47, 54, 128, 102, 103, 102, 133, 102, 106]
flag = ""
for _ in range(len(bytes)):
    tmp = bytes[_] + 35
    tmp -= 17
    tmp ^= 5
    tmp -= 17
    tmp ^= 5
    tmp -= 5
    tmp ^= 5
    flag += chr(tmp)

print(flag[::-1])

# OUTPUT : mazala{14ZY_0r_8U5Y}