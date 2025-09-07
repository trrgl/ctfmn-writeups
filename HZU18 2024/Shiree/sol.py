# Америк мужан = ASCII

wood = [72, 313, 531, 718, 948, 1238, 1415, 1613, 1891, 2112, 2340, 2556, 2779, 3002, 3217, 3429, 3632, 3888, 4112, 4345, 4511, 4808] # ugsun utguud
flag = ""
for i in range(len(wood)):
    flag += chr(wood[i] % 223)

print(flag)

# OUTPUT : HZU18{M4kinggg_T@abl3}