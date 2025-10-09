# 1. .class file gdgi file command aar harna.
# 2. decompile hiiged reverse hiine
enc = [13, 159, 144, 4, 61, 126, 146, 6, 106, 49, 71, 6, 106, 49, 4, 4, 106, 48, 50, 4, 4, 4, 106, 4, 6, 49, 71, 155, 4, 155, 51, 72]
flag = ""
for i in enc:
    ch = i ^ 25
    ch += 52
    ch ^= 52
    ch -= 52
    flag += chr(ch)

print(flag)

# OUTPUT : HZU18{W3_4r3_411_57111_134rN1N6}